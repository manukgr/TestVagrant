from locators.ndtv_main_page_locators import NdtvMainPageLocators
from locators.ndtv_weather_page_locators import NdtvWeatherPageLocators
from page_objects.base_page import BasePage
from page_objects.ndtv_main_page import NdtvMainPage


class NdtvWeatherPage(BasePage, NdtvWeatherPageLocators):

        def launch_page(self):
            NdtvMainPage().navigate_to_weather_page()
