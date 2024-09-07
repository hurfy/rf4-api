from celery.schedules     import crontab
from celery               import signals

from apps.parser.services import WebParser, create_driver, records_urls, ratings_urls, DBRecords, DBRatings
from worker               import app


def fetch_records() -> None:
    """
    Fetches fish records from the game's website and saves them to the database.
    Retrieves the records table from the website for each region and category,
    parses the data into a dictionary of fish records, and saves the records to
    the database using `DBRecords`
    """
    web_parser = WebParser(create_driver())
    db_records = DBRecords()
    records    = {}

    for region in (urls := records_urls()):
        for category in (categories := urls[region]):
            data = web_parser.parse_records_table(categories[category], region, category)

            if not records:
                records = data

            else:
                for fish in data:
                    records[fish].extend(data[fish])

    db_records.create(records)


def fetch_ratings() -> None:
    """
    Fetches player ratings from the game's website and saves them to the database.
    Retrieves the ratings table from the website for each region,
    parses the data into a list of player ratings, and saves the ratings to
    the database using `DBRatings`
    """
    web_parser = WebParser(create_driver())
    db_ratings = DBRatings()
    ratings    = []

    for region in ratings_urls():
        ratings.extend(
            web_parser.parse_ratings_table(ratings_urls()[region], region)
        )

    db_ratings.create(ratings)


@app.task(bind=True, ignore_result=True)
def fetch_records_at_worker_ready(self) -> None:
    fetch_records()


@app.task(bind=True, ignore_result=True)
def fetch_ratings_at_worker_ready(self) -> None:
    fetch_ratings()


# TODO: Add daily tasks
@signals.worker_ready.connect()
def at_worker_ready(**kwargs) -> None:
    fetch_records_at_worker_ready.delay()
    fetch_ratings_at_worker_ready.delay()
