import time
import unittest

from page_objects.ndtv_main_page import NdtvMainPage


class NdtvMainPageTests(unittest.TestCase):

    ndtv_main_page = NdtvMainPage()

    def setUp(self) -> None:
        self.ndtv_main_page.register_driver("chrome", " 87.0.4280.88")

    def test_01_verify_that_ndtv_site_is_working_as_expected(self):
        self.ndtv_main_page.open('')


