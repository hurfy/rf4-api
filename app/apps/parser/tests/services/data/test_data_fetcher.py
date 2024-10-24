from django.test          import TestCase

from apps.parser.services import WebDriver, URLsManager, RecordsFetcher, RatingsFetcher, WinnersFetcher


class RecordsFetcherTestCase(TestCase):
    def setUp(self) -> None:
        self.fetcher = RecordsFetcher(
            WebDriver(),
            URLsManager(),
        )

    def test_get_absolute_records_urls(self) -> None:
        data = self.fetcher._get_urls()

        self.assertIsInstance(data, tuple), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)

        self.assertEqual(data[0], "records_wrapper")
        self.assertIsInstance(data[1], dict), self.assertTrue(data[1]), self.assertIsNotNone(data[1])

    def test_get_weekly_records_urls(self) -> None:
        data = self.fetcher._get_urls(weekly = True)

        self.assertIsInstance(data, tuple), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)

        self.assertEqual(data[0], "records_wrapper")
        self.assertIsInstance(data[1], dict), self.assertTrue(data[1]), self.assertIsNotNone(data[1])

    def test_fetch_absolute_records(self) -> None:
        for data in self.fetcher.fetch():
            self.assertIsInstance(data, tuple), self.assertTrue(data), self.assertIsNotNone(data)
            self.assertEqual(len(data), 3)

            self.assertIsInstance(data[2], str), self.assertTrue(data[2]), self.assertIsNotNone(data[2])

    def test_fetch_weekly_records(self) -> None:
        for data in self.fetcher.fetch(weekly = True):
            self.assertIsInstance(data, tuple), self.assertTrue(data), self.assertIsNotNone(data)
            self.assertEqual(len(data), 3)

            self.assertIsInstance(data[2], str), self.assertTrue(data[2]), self.assertIsNotNone(data[2])


class RatingsFetcherTestCase(TestCase):
    def setUp(self) -> None:
        self.fetcher = RatingsFetcher(
            WebDriver(),
            URLsManager(),
        )

    def test_get_ratings_urls(self) -> None:
        data = self.fetcher._get_urls()

        self.assertIsInstance(data, tuple), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)

        self.assertEqual(data[0], "ratings")
        self.assertIsInstance(data[1], dict), self.assertTrue(data[1]), self.assertIsNotNone(data[1])

    def test_fetch_ratings(self) -> None:
        for data in self.fetcher.fetch():
            self.assertIsInstance(data, tuple), self.assertTrue(data), self.assertIsNotNone(data)
            self.assertEqual(len(data), 3)

            self.assertIsInstance(data[2], str), self.assertTrue(data[2]), self.assertIsNotNone(data[2])


class WinnersFetcherTestCase(TestCase):
    def setUp(self) -> None:
        self.fetcher = WinnersFetcher(
            WebDriver(),
            URLsManager(),
        )

    def test_get_ratings_urls(self) -> None:
        data = self.fetcher._get_urls()

        self.assertIsInstance(data, tuple), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)

        self.assertEqual(data[0], "records")
        self.assertIsInstance(data[1], dict), self.assertTrue(data[1]), self.assertIsNotNone(data[1])

    def test_fetch_ratings(self) -> None:
        for data in self.fetcher.fetch():
            self.assertIsInstance(data, tuple), self.assertTrue(data), self.assertIsNotNone(data)
            self.assertEqual(len(data), 3)

            self.assertIsInstance(data[2], str), self.assertTrue(data[2]), self.assertIsNotNone(data[2])