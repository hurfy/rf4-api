from django.test          import TestCase

from selenium             import webdriver

from apps.parser.services import create_driver


class SeleniumWebDriverTestCase(TestCase):
    def setUp(self) -> None:
        self.driver = create_driver()

    def test_create_driver(self) -> None:
        self.assertIsInstance(self.driver, webdriver.Chrome)
        # self.assertEquals(self.driver.capabilities["browserName"], "chrome-headless-shell")
        self.assertEquals(self.driver.capabilities["browserName"], "chrome")
