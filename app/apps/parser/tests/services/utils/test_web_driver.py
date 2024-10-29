from django.test          import TestCase
from selenium             import webdriver

from apps.parser.services import WebDriver


class WebDriverTestCase(TestCase):
    def setUp(self) -> None:
        self.driver = WebDriver()

    def test_fetch_raw_html(self) -> None:
        data = self.driver.fetch_raw_html("https://nohello.net/ru/", "container")

        self.assertIsInstance(data, str), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertIn("<div id=\"plsstop\">", data)

    def test_driver(self) -> None:
        data = self.driver.driver

        self.assertIsInstance(data, webdriver.Chrome), self.assertTrue(data), self.assertIsNotNone(data)

        data = self.driver.driver.capabilities

        self.assertIsInstance(data, dict), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEquals(data["browserName"], "chrome")
