from abc                       import ABC, abstractmethod
from bs4                       import BeautifulSoup

from apps.parser.services.data import AbstractFetcher, RecordsFetcher, RatingsFetcher, WinnersFetcher
from apps.parser.services      import DataProcessor, WebDriver, URLsManager


class AbstractParser(ABC):
    def __init__(self, fetcher: AbstractFetcher) -> None:
        self.__fetcher = fetcher

    @abstractmethod
    def _serialize_data(self, data, region: str, *args, **kwargs) -> dict:
        """Get and serialize data from HTML"""
        pass

    @abstractmethod
    def _parse_data(self, data, region: str, *args, **kwargs) -> list[dict]:
        """Search and process information from HTML"""
        pass

    def parse(self, *args, **kwargs) -> dict:
        """Wrapper for parsing all tables"""
        fetched_data = self.__fetcher.fetch(*args, **kwargs)

        for data in fetched_data:
            region, category, data = data

            yield self._parse_data(data, region, category = category)


class RecordsParser(AbstractParser):
    def _serialize_data(self, data, region: str, *args, **kwargs) -> dict:
        dp = DataProcessor()

        return {
            "category": kwargs.get("category", "records"),
            "region"  : region.lower(),
            "player"  : dp.clean(data.find("div", class_ = "gamername").text.strip()),
            "fish"    : dp.clean(kwargs.get("fish", "").strip()),
            "weight"  : dp.to_kg(data.find("div", class_ = "weight").text),
            "location": dp.clean(data.find("div", class_ = "location").text),
            "bait"    : dp.clean(data.find("div", class_ = "bait_icon").get("title")),
            "date"    : dp.serialize(data.find("div", class_ = "data").text),
        }

    def _parse_data(self, data, region: str, *args, **kwargs) -> list[dict]:
        records = []
        soup    = BeautifulSoup(data, "html.parser")

        # Looking for records on each fish
        for fish in soup.find_all(attrs = {"class": "rows"})[0]:
            # Each record can have up to 5 records, look for them
            sub_records = []
            rows        = fish.find_all(attrs = {"class": "row"})

            # No records found
            if len(rows) <= 1:
                continue

            for row in rows:
                sub_records.append(
                    self._serialize_data(
                        row,
                        region,
                        fish     = fish.find("div", class_ = "text").text,
                        category = kwargs.get("category", "records")
                    )
                )

            records.extend(sub_records)

        return records


class RatingsParser(AbstractParser):
    def _serialize_data(self, data, region: str, *args, **kwargs) -> dict:
        return {
            "region"  : region.lower(),
            "player"  : data.find("div", class_ = "avatar_text").text,
            "position": int(data.find("td", class_ = "position").text),
            "level"   : int(data.find("td", class_ = "level").text),
            "ingame"  : int(data.find("td", class_ = "gametime").text),
        }

    def _parse_data(self, data, region: str, *args, **kwargs) -> list[dict]:
        ratings = []
        soup    = BeautifulSoup(data, "html.parser")

        for row in soup.find_all(attrs = {"class": "highlight"}):
            ratings.append(
                self._serialize_data(row, region)
            )

        return ratings


class WinnersParser(AbstractParser):
    def _serialize_data(self, data, region: str, *args, **kwargs) -> dict:
        return {
            "category": kwargs.get("category", "records"),
            "region"  : region.lower(),
            "player"  : data.find("div", class_ = "avatar_text").text,
            "position": int(data.find("td", class_ = "position").text),
            "records" : int(data.find("td", class_ = "records").text),
            "score"   : int(data.find("td", class_ = "score").text.replace(" ", "")),
            "prize"   : data.find("td", class_ = "prize").text,
        }

    def _parse_data(self, data, region: str, *args, **kwargs) -> list[dict]:
        winners = []
        soup    = BeautifulSoup(data, "html.parser")

        for row in soup.find_all(attrs = {"class": "highlight"}):
            winners.append(
                self._serialize_data(
                    row,
                    region,
                    category = kwargs.get("category", "records")
                )
            )

        return winners


class ParsersManager:
    PARSERS = {
        "records": (RecordsFetcher, RecordsParser),
        "ratings": (RatingsFetcher, RatingsParser),
        "winners": (WinnersFetcher, WinnersParser),
    }

    def create(self, name: str = "records") -> AbstractParser:
        """Parser config for selected table"""
        fetcher_name, parser_name = self.PARSERS.get(name, "records")

        return parser_name(
            fetcher = fetcher_name(
                WebDriver(),
                URLsManager()
            )
        )