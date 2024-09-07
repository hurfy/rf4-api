from selenium.webdriver.common.by import By
from selenium                     import webdriver
from bs4                          import BeautifulSoup
from re                           import findall


class WebParser:
    def __init__(self, driver: webdriver) -> None:
        self.__driver = driver

    def __fetch_table(self, url, class_name: str) -> str:
        """
        Fetches the records table from the given URL and returns it as HTML
        """
        self.__driver.get(url)
        self.__driver.implicitly_wait(3)  # 3 seconds

        return self.__driver.find_element(By.CLASS_NAME, class_name).get_attribute("outerHTML")

    # TODO: refactor this pls...
    def parse_records_table(self, url, rg, r_type: str) -> dict:
        """
        This function parses the records table from a given URL and returns a dictionary of records
        """
        records = {}
        soup    = BeautifulSoup(self.__fetch_table(url, "records_wrapper"), "html.parser")

        # Looking for records on each fish
        for fish in soup.find_all(attrs={"class": "rows"})[0]:
            _records  = []
            fish_name = fish.find("div", class_="text").text

            # Each record can have up to 5 records, look for them
            rows = fish.find_all(attrs={"class": "row"})

            # No records found
            if len(rows) <= 1:
                continue

            else:
                for row in rows:
                    _records.append(
                        {
                            "weight":
                                self.__convert_to_kilograms(
                                    self.__replace_html_chars(row.find("div", class_="weight").text)
                                ),
                            "location":
                                self.__replace_html_chars(row.find("div", class_="location").text),
                            "bait":
                                self.__replace_html_chars(row.find("div", class_="bait_icon").get('title')),
                            "username":
                                self.__replace_html_chars(row.find("div", class_="gamername").text.strip()),
                            "date":
                                self.__convert_to_db_date(
                                    self.__replace_html_chars(row.find("div", class_="data").text)
                                ),
                            "region":
                                rg.lower(),
                            "type":
                                r_type,
                        }
                    )

            records[fish_name.strip()] = _records

        return records

    def parse_ratings_table(self, url, rg: str) -> list[dict]:
        """
        This function parses the ratings table from a given URL using BeautifulSoup.
        It takes a URL as input, fetches the ratings table, and returns a list of dictionaries
        """
        ratings = []
        soup    = BeautifulSoup(self.__fetch_table(url, "rating"), "html.parser")

        for row in soup.find_all(attrs={"class": "highlight"}):
            ratings.append(
                {
                    "position": int(row.find("td", class_="position").text),
                    "username": row.find("div", class_="avatar_text").text,
                    "level"   : int(row.find("td", class_="level").text),
                    "gametime": int(row.find("td", class_="gametime").text),
                    "region"  : rg.lower(),
                }
            )

        return ratings

    @staticmethod
    def __replace_html_chars(text: str) -> str:
        return text.replace("\xa0", "")

    @staticmethod
    def __convert_to_kilograms(text: str) -> float:
        return float(
            int("".join([i for i in findall(r"\d+", text)])) / 1000
        )

    @staticmethod
    def __convert_to_db_date(text: str) -> str:
        _list = text.split(".")

        return f"20{_list[2]}-{_list[1]}-{_list[0]}"
