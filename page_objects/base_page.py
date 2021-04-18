import testdata.urls as url
from page_objects.driver_factory import DriverFactory


class BasePage:
    def __init__(self):
        self.base_url = url.ndtv_url
        self.driver_obj = DriverFactory()
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
        self.driver.get(self.base_url+url)

