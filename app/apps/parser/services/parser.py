from selenium.webdriver.common.by import By
from selenium                     import webdriver
from bs4                          import BeautifulSoup
from re                           import findall


class WebParser:
    def __init__(self, driver: webdriver) -> None:
        self.__driver = driver

    def __fetch_table(self, url: str, class_name: str) -> str:
        """
        Fetches the records table from the given URL and returns it as HTML
        """
        self.__driver.get(url)
        self.__driver.implicitly_wait(1)  # 1 second

        return self.__driver.find_element(By.CLASS_NAME, class_name).get_attribute("outerHTML")

    def parse_records_table(self, url: str) -> dict:
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
            for row in fish.find_all(attrs={"class": "row"}):
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
                            self.__replace_html_chars(row.find("div", class_="data").text)
                    }
                )

            records[fish_name] = _records

        return records

    def parse_ratings_table(self, url: str) -> list[dict]:
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
                    "level"   : row.find("td", class_="level").text,
                    "gametime": row.find("td", class_="gametime").text
                }
            )

        return ratings

    @staticmethod
    def __replace_html_chars(text: str) -> str:
        return text.replace("\xa0", "")

    @staticmethod
    def __convert_to_kilograms(text: str) -> int:
        return int(
            int("".join([i for i in findall(r"\d+", text)])) / 1000
        )