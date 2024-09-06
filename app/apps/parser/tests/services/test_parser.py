from django.test          import TestCase

from pydantic             import BaseModel, ValidationError
from typing               import Dict, List

from apps.parser.services import WebParser, create_driver, records_urls, ratings_urls


class BaseRecord(BaseModel):
    username: str
    region  : str


class Record(BaseRecord):
    weight  : float
    location: str
    bait    : str
    date    : str
    type    : str


class Rating(BaseRecord):
    position: int
    level   : int
    gametime: int


class Records(BaseModel):
    data: Dict[str, List[Record]]


class Ratings(BaseModel):
    data: List[Rating]


class WebParserTestCase(TestCase):
    def setUp(self) -> None:
        self.parser  = WebParser(create_driver())
        self.records = records_urls()
        self.ratings = ratings_urls()

    def test_parse_records_table(self) -> None:
        try:
            Records(
                data=self.parser.parse_records_table(
                    self.records["GL"]["records"],
                    "GL",
                    "records",
                )
            )

        except ValidationError as e:
            self.fail(f"ValidationError: {e}")

    def test_parse_ratings_table(self) -> None:
        try:
            Ratings(
                data=self.parser.parse_ratings_table(
                    self.ratings["GL"],
                    "GL",
                )
            )

        except ValidationError as e:
            self.fail(f"ValidationError: {e}")
