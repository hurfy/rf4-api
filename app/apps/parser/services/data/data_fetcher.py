from apps.parser.services import URLsManager, WebDriver
from abc                  import ABC, abstractmethod


class AbstractFetcher(ABC):
    def __init__(self, driver: WebDriver, urls: URLsManager) -> None:
        self.__driver = driver
        self._urls    = urls

    @abstractmethod
    def _get_urls(self, *args, **kwargs) -> tuple[str, dict]:
        """Generating a list of record table URLs"""
        pass

    def fetch(self, *args, **kwargs) -> tuple[str, str or None, str]:
        """Fetching raw HTML for parsing"""
        class_name, urls = self._get_urls(*args, **kwargs)

        for key, value in urls.items():
            if not isinstance(value, dict):
                yield key, None, self.__driver.fetch_raw_html(value, class_name)

            else:
                for sub_key, sub_value in value.items():
                    yield key, sub_key, self.__driver.fetch_raw_html(sub_value, class_name)


class RecordsFetcher(AbstractFetcher):
    def _get_urls(self, *args, **kwargs) -> tuple[str, dict]:
        return "records_wrapper", self._urls.records_urls(kwargs.get("weekly", False))


class RatingsFetcher(AbstractFetcher):
    def _get_urls(self, *args, **kwargs) -> tuple[str, dict]:
        return "ratings", self._urls.ratings_urls()


class WinnersFetcher(AbstractFetcher):
    def _get_urls(self, *args, **kwargs) -> tuple[str, dict]:
        return "records", self._urls.winners_urls()