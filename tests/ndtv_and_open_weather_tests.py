import unittest

from endpoints import weather_api
from page_objects.ndtv_weather_page import NdtvWeatherPage
from testdata import variation


class NdtvOpenWeatherTests(unittest.TestCase):
    ndtv_weather_page = NdtvWeatherPage()

    def setUp(self) -> None:
        self.ndtv_weather_page.register_driver("87.0.4280.88")
        self.ndtv_weather_page.launch_page()

    def tearDown(self) -> None:
        self.ndtv_weather_page.driver.quit()

    def test_01_verify_that_weather_reported_by_website_and_apis_is_comparable(self):
        """
        Test to validate if Temperature shown over Open Weather Map API and NDTV Weather UI is comparable
        :return:
        """
        search_box = self.ndtv_weather_page.get_element(self.ndtv_weather_page.search_box)
        search_box.send_keys("Chandigarh")
        self.ndtv_weather_page.get_element(self.ndtv_weather_page.city).click()
        self.assertTrue(self.ndtv_weather_page.get_element
                        (self.ndtv_weather_page.city_weather_info_on_map).is_displayed())
        temp_api = int(float(weather_api.get_temperature("Chandigarh")))
        temp_ui = self.ndtv_weather_page.get_element(self.ndtv_weather_page.city_weather_info_on_map).text
        temp_ui = int(float(temp_ui.split('℃')[0]))
        print(temp_api + temp_ui)
        self.assertLessEqual(abs(temp_ui-temp_api), variation.tolerable_degrees,
                             "Variation of temperatures is exceeding tolerable degrees")
