from django.test          import TestCase

from apps.parser.services import (RecordsParser, RatingsParser, WinnersParser, ParsersManager, RecordsFetcher,
                                  RatingsFetcher, WinnersFetcher, WebDriver, URLsManager)


class TestRecordsParser(TestCase):
    def setUp(self) -> None:
        self.parser = RecordsParser(
            RecordsFetcher(
                WebDriver(),
                URLsManager(),
            )
        )

    def test_parse_absolute_records(self) -> None:
        pass

    def test_parse_weekly_records(self) -> None:
        pass


class TestRatingsParser(TestCase):
    def setUp(self) -> None:
        self.parser = RatingsParser(
            RatingsFetcher(
                WebDriver(),
                URLsManager(),
            )
        )

    def test_parse(self) -> None:
        pass


class TestWinnersParser(TestCase):
    def setUp(self) -> None:
        self.parser = WinnersParser(
            WinnersFetcher(
                WebDriver(),
                URLsManager(),
            )
        )

    def test_parse(self) -> None:
        pass


class TestParsersManager(TestCase):
    def setUp(self) -> None:
        self.pm = ParsersManager

    def create_records_parser(self) -> None:
        pass

    def create_ratings_parser(self) -> None:
        pass

    def create_winners_parser(self) -> None:
        pass
