from apps.parser.services import ParsersManager, DBProcessor
from worker               import app


@app.task(autoretry_for=(Exception,), retry_kwargs={"max_retries": 7, "countdown": 5})
def process_data(parser_name, model_name: str, *args, **kwargs) -> None:
    parser = ParsersManager.create(parser_name)
    data   = []

    # parse data
    raw_data = parser.parse() \
        if (weekly := kwargs.get("weekly", False)) \
        else parser.parse(weekly)

    # unpack data
    for each in raw_data:
        data.extend(each)

    # write data to db
    DBProcessor.write(
        model_name,
        data
    )


# process_data.delay("records", "AbsoluteRecord")
# process_data.delay("records", "WeeklyRecord")
# process_data.delay("ratings", "Rating")
# process_data.delay("winners", "Winner")
