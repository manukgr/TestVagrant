"""
DriverFactory class
NOTE: Change this class as you add support for:
1. Cloud Drivers
2. Mobile Drivers
"""

from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as firefoxOptions

from utils import command_line


class DriverFactory:

    def __init__(self,browser_version=None, os_name=None):
        "Constructor for the Driver factory"
        self.browser_version = browser_version
        self.os_name = os_name

    def get_web_driver(self, browser_version):
        """ Other Drivers can be added """
        web_driver = self.run_local(browser_version)

        return web_driver

    def run_local(self, browser_version):
        """
        Return the local driver
        : TODO Add support to other browsers
        """
        if command_line.get_browser().lower() == "chrome":
            options = chromeOptions()
            options.add_argument("disable-infobars")
            if command_line.headless() == "y":
                options.add_argument("--headless")  # For Headless chrome
            caps = DesiredCapabilities.CHROME
            local_driver = webdriver.Chrome(options=options, desired_capabilities=caps)
            return local_driver

        if command_line.get_browser().lower() == "ff" \
            or command_line.get_browser().lower() == "firefox":
            profile = FirefoxProfile()
            options = firefoxOptions()

            profile.set_preference("geo.prompt.testing", True)
            profile.set_preference("geo.prompt.testing.allow", True)
            if command_line.headless() == "y":
                options.headless = True  # For Headless firefox
            local_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                             firefox_profile=profile, options=options)
            return local_driver
