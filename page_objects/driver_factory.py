"""
DriverFactory class
NOTE: Change this class as you add support for:
1. Cloud Drivers
2. Mobile Drivers
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary

class DriverFactory:

    def __init__(self, browser='ff', browser_version=None, os_name=None):
        "Constructor for the Driver factory"
        self.browser = browser
        self.browser_version = browser_version
        self.os_name = os_name

    def get_web_driver(self, browser, browser_version):
        """ Other Drivers can be added """
        web_driver = self.run_local(browser, browser_version)

        return web_driver

    def run_local(self, browser, browser_version):
        """
        Return the local driver
        : TODO Add support to other browsers
        """
        options = chromeOptions()
        options.add_argument("disable-infobars")
        #options.add_argument("--headless")  # For Headless chrome
        caps = DesiredCapabilities.CHROME
        local_driver = webdriver.Chrome(options=options, desired_capabilities=caps)
        return local_driver
