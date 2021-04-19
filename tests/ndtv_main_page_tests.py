import time
import unittest

from page_objects.ndtv_main_page import NdtvMainPage


class NdtvMainPageTests(unittest.TestCase):

    ndtv_main_page = NdtvMainPage()

    def setUp(self) -> None:
        self.ndtv_main_page.register_driver("chrome", " 87.0.4280.88")
        self.ndtv_main_page.open('')

    def tearDown(self) -> None:
        self.ndtv_main_page.driver.quit()

    def test_01_verify_that_ndtv_site_is_working_as_expected(self):
        self.assertEquals(self.ndtv_main_page.driver.title,
                          "Get Latest News, India News, Breaking News, Today's News - NDTV.com"
                          ,"Tilte Mismatch")

    def test_02_verify_that_notification_popup_is_appearing_on_main_page(self):
        elm = self.ndtv_main_page.get_element(self.ndtv_main_page.no_thanks_button)
        self.assertTrue(elm.is_displayed(), "Element No Thanks Button is not displayed")

