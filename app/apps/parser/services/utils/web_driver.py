from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by      import By
from selenium                          import webdriver


class WebDriver:
    def __init__(self) -> None:
        user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/127.0.0.0 Safari/537.36"
        )
        options_list = [
            "--headless",
            "--disable-gpu",
            "--disable-extensions",
            "--disable-images",
            "--disable-css",
            f"--user-agent={user_agent}"
        ]

        options = Options()

        for option in options_list:
            options.add_argument(option)

        self._driver = webdriver.Chrome(options = options)

    def fetch_raw_html(self, url: str, class_name: str) -> str:
        """Get a whole HTML page from which data will be extracted later on"""
        self._driver.get(url)
        self._driver.implicitly_wait(1)  # 1 second delay

        return self._driver.find_element(By.CLASS_NAME, class_name).get_attribute("outerHTML")

    @property
    def driver(self) -> webdriver:
        return self._driver

