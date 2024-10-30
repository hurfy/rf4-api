from django.conf import settings


class URLsManager:
    __REGIONS    = ["GL", "RU", "DE", "US", "FR", "CN", "PL", "KR", "JP", "EN"]
    __CATEGORIES = ["records", "ultralight", "telestick"]

    def __init__(self) -> None:
        self.region = self._initialize_region()

    def records_urls(self, weekly: bool = False) -> dict:
        url = "https://rf4game.{}/{}/region/{}/"

        if weekly:
            url = "https://rf4game.{}/{}/weekly/region/{}/"

        return {
            rg: {
                ct: url.format(self.region, ct, rg)
                for ct in self.__CATEGORIES
            }
            for rg in self.__REGIONS
        }

    def ratings_urls(self) -> dict:
        return {
            rg:
                f"https://rf4game.{self.region}/ratings/region/{rg}/"
            for rg in self.__REGIONS
        }

    def winners_urls(self) -> dict:
        return {
            rg: {
                ct: f"https://rf4game.{self.region}/{ct}/winners/region/{rg}/"
                for ct in self.__CATEGORIES
            }
            for rg in self.__REGIONS
        }

    @property
    def regions(self) -> list[str]:
        return self.__REGIONS

    @property
    def categories(self) -> list[str]:
        return self.__CATEGORIES

    @staticmethod
    def _initialize_region() -> str:
        match region := settings.PARSER_REGION:
            case "ru" | "pl" | "de" | "jp" | "kr":
                return region

            case "cn" | "fr":
                return f"com/{region}"

            case _:
                return "com"