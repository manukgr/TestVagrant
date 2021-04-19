from locators.ndtv_main_page_locators import NdtvMainPageLocators
from page_objects.base_page import BasePage


class NdtvMainPage(BasePage, NdtvMainPageLocators):

    def navigate_to_weather_page(self):
        self.open('')
        self.get_element(NdtvMainPageLocators.no_thanks_button).click()
        self.get_element(NdtvMainPageLocators.overflow_button_nav_bar).click()
        self.get_element(NdtvMainPageLocators.weather_button_nav_bar).click()
