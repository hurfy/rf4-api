from selenium                          import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver() -> webdriver.Chrome:
    """
    Creates a new instance of the Chrome webdriver with specified options
    """
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

    # Add options
    for option in options_list:
        options.add_argument(option)

    return webdriver.Chrome(options=options)