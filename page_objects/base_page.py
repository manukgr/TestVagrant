import unittest

from selenium.webdriver.support.wait import WebDriverWait

import testdata.urls as url
from page_objects.driver_factory import DriverFactory
from selenium.webdriver.support import expected_conditions as EC


def write(msg):
    print(msg)


class Borg:
    # The borg design pattern is to share state
    # Src: http://code.activestate.com/recipes/66531/
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def is_first_time(self):
        """ Has the child class been invoked before? """
        result_flag = False
        if len(self.__dict__) == 0:
            result_flag = True
        return result_flag


class BasePage(Borg, unittest.TestCase):
    def __init__(self):
        """ Constructor """
        Borg.__init__(self)
        if self.is_first_time():
            self.driver = None
            self.result_flag = False
        self.base_url = url.ndtv_url
        self.driver_obj = DriverFactory()
        if self.driver is not None:
            self.launch_page()

    def launch_page(self):
        """Overwrite this method in your Page module if you want to visit a specific URL"""
        pass

    def register_driver(self, browser, browser_version):
        """
        Register Driver for various browsers based on command line arguments
        :param browser:
        :param browser_version:
        :return:
        """
        self.driver = self.driver_obj.get_web_driver(browser, browser_version)

    def open(self, url):
        """
        Launch or move to other page on website
        :param url:
        :return:
        """
        self.driver.get(self.base_url + url)

    def split_locator(self, locator):
        """ Split the locator type and locator """
        try:
            loc = locator.split(',')
            if loc[0] == "css":
                loc[0] = "css selector"
            return tuple([loc[0], loc[1]])

        except Exception as e:
            write("Error while parsing locator")
            raise e

    def get_element(self, locator, timeout=20):
        """

        :param locator:
        :param timeout:
        :param retry_interval:
        :return:
        """
        dom_element = None
        path = self.split_locator(locator)
        try:
            self.smart_wait(timeout, locator)
            dom_element = self.driver.find_element(*path)
            self.smart_wait(timeout, locator)
            return dom_element
        except Exception as e:
            write("Error While getting locator")
            raise e

    def smart_wait(self, wait_seconds, locator):
        path = self.split_locator(locator)
        WebDriverWait(self.driver, wait_seconds).until(EC.presence_of_element_located(path))
