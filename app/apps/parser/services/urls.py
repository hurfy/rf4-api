# International, Russia&CIS, Germany, USA, France, China, Poland, Korea, Japan, Other
REGIONS = ["GL", "RU", "DE", "US", "FR", "CN", "PL", "KR", "JP", "EN"]
# Records, Ultralight, Telestick
CATEGORY_URL = ["records", "ultralight", "telestick"]


def fish_ratings_urls() -> list[str]:
    """
    Returns a list of URLs for fish ratings across different regions and categories.
    This function iterates over the defined regions and categories, generating a URL for each combination
    """
    urls: list[str] = []

    for region in REGIONS:
        for category in CATEGORY_URL:
            urls.append(f"https://rf4game.ru/{category}/region/{region}/")

    return urls


def player_ratings_url() -> list[str]:
    """
    Returns a list of URLs for player ratings across different regions
    """
    return [f'https://rf4game.ru/ratings/{region}/' for region in REGIONS]