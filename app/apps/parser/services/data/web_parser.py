from abc                       import ABC, abstractmethod
from bs4                       import BeautifulSoup

from apps.parser.services.data import AbstractFetcher
from apps.parser.services      import DataProcessor


class AbstractParser(ABC):
    def __init__(self, fetcher: AbstractFetcher) -> None:
        self.__fetcher = fetcher

    @abstractmethod
    def _serialize_data(self, data, region: str, *args, **kwargs) -> dict:
        pass

    @abstractmethod
    def _parse_data(self, data, region: str, *args, **kwargs) -> list[dict]:
        pass

    def parse(self, *args, **kwargs) -> dict:
        fetched_data = self.__fetcher.fetch(*args, **kwargs)

        for data in fetched_data:
            region, category, data = data

            yield self._parse_data(data, region, category=category)


class RecordsParser(AbstractParser):
    def _serialize_data(self, data, region: str, *args, **kwargs) -> dict:
        dp = DataProcessor()

        return {
            "fish"    : dp.rm_html_chars(kwargs.get("fish", "").strip()),
            "region"  : region.lower(),
            "type"    : kwargs.get("category", "records"),
            "weight"  : dp.convert_to_kg(data.find("div", class_="weight").text),
            "location": dp.rm_html_chars(data.find("div", class_="location").text),
            "bait"    : dp.rm_html_chars(data.find("div", class_="bait_icon").get('title')),
            "username": dp.rm_html_chars(data.find("div", class_="gamername").text.strip()),
            "date"    : dp.serialize_date(data.find("div", class_="data").text),
        }

    def _parse_data(self, data, region: str, *args, **kwargs) -> list[dict]:
        records = []
        soup    = BeautifulSoup(data, "html.parser")

        # Looking for records on each fish
        for fish in soup.find_all(attrs={"class": "rows"})[0]:
            # Each record can have up to 5 records, look for them
            sub_records = []
            rows        = fish.find_all(attrs={"class": "row"})

            # No records found
            if len(rows) <= 1:
                continue

            for row in rows:
                sub_records.append(
                    self._serialize_data(
                        row,
                        region,
                        fish     = fish.find("div", class_="text").text,
                        category = kwargs.get("category", "records")
                    )
                )

            records.extend(sub_records)

        return records


class RatingsParser(AbstractParser):
    def _serialize_data(self, data, region: str, *args, **kwargs) -> dict:
        return {
            "position": int(data.find("td", class_="position").text),
            "username": data.find("div", class_="avatar_text").text,
            "level"   : int(data.find("td", class_="level").text),
            "gametime": int(data.find("td", class_="gametime").text),
            "region"  : region.lower(),
        }

    def _parse_data(self, data, region: str, *args, **kwargs) -> list[dict]:
        ratings = []
        soup    = BeautifulSoup(data, "html.parser")

        for row in soup.find_all(attrs={"class": "highlight"}):
            ratings.append(
                self._serialize_data(row, region)
            )

        return ratings


# WIP
class WinnersParser(AbstractParser):
    def _serialize_data(self, data, region: str, *args, **kwargs) -> dict:
        pass

    def _parse_data(self, data, region: str, *args, **kwargs) -> list[dict]:
        pass
