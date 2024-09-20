class URLsManager:
    __REGIONS    = ["GL", "RU", "DE", "US", "FR", "CN", "PL", "KR", "JP", "EN"]
    __CATEGORIES = ["records", "ultralight", "telestick"]

    def records_urls(self, weekly: bool = False) -> dict:
        url = "https://rf4game.ru/{}/region/{}/"

        if weekly:
            url = "https://rf4game.ru/{}/weekly/region/{}/"

        return {
            rg: {
                ct: url.format(ct, rg)
                for ct in self.__CATEGORIES
            }
            for rg in self.__REGIONS
        }

    def ratings_urls(self) -> dict:
        return {
            rg:
                f"https://rf4game.ru/ratings/region/{rg}/"
            for rg in self.__REGIONS
        }

    def winners_urls(self) -> dict:
        return {
            rg: {
                ct: f"https://rf4game.ru/{ct}/winners/region/{rg}/"
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
