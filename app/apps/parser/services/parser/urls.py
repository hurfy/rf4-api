# International, Russia&CIS, Germany, USA, France, China, Poland, Korea, Japan, Other
REGIONS = ["GL", "RU", "DE", "US", "FR", "CN", "PL", "KR", "JP", "EN"]
# Records, Ultralight, Telestick
CATEGORY_URL = ["records", "ultralight", "telestick"]


def records_urls() -> dict:
    """
    Returns a list of URLs for fish ratings across different regions and categories.
    This function iterates over the defined regions and categories, generating a URL for each combination
    """
    return {
        rg: {
            ct: f"https://rf4game.ru/{ct}/region/{rg}/"
            for ct in CATEGORY_URL
        }
        for rg in REGIONS
    }


def ratings_urls() -> dict:
    """
    Returns a dictionary of URLs for player ratings across different regions.
    The dictionary keys are region codes, and the values are URLs for the corresponding region's player ratings
    """
    return {
        rg:
            f'https://rf4game.ru/ratings/region/{rg}/'
        for rg in REGIONS
    }
