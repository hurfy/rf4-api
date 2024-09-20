from django.test          import TestCase

from apps.parser.services import URLsManager


class URLsManagerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.manager = URLsManager()

    def test_urls_records(self) -> None:
        data = self.manager.records_urls()

        self.assertIsInstance(data, dict), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertIsInstance(data["GL"], dict)
        self.assertIsInstance(data["GL"]["records"], str)

        data = self.manager.records_urls(weekly=True)

        self.assertIsInstance(data, dict), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertIsInstance(data["GL"], dict)
        self.assertIsInstance(data["GL"]["records"], str)

    def test_urls_ratings(self) -> None:
        data = self.manager.ratings_urls()

        self.assertIsInstance(data, dict), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertIsInstance(data["GL"], str)

    def test_urls_winners(self) -> None:
        data = self.manager.records_urls()

        self.assertIsInstance(data, dict), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertIsInstance(data["GL"], dict)
        self.assertIsInstance(data["GL"]["records"], str)

    def test_regions(self) -> None:
        data = self.manager.regions

        self.assertIsInstance(data, list), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(data, ["GL", "RU", "DE", "US", "FR", "CN", "PL", "KR", "JP", "EN"])

    def test_categories(self) -> None:
        data = self.manager.categories

        self.assertIsInstance(data, list), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(data, ["records", "ultralight", "telestick"])


