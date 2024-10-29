from decouple import config


def get_variable(name: str) -> str:
    var = config(name)

    if var.startswith("<") or not var:
        raise Exception(f"Invalid or missing {var} in the .env file")

    return var


# Django
DJANGO_KEY  : str = get_variable("DJANGO_KEY")

# Postgres
PG_USERNAME : str  = get_variable("POSTGRES_USERNAME")
PG_PASSWORD : str  = get_variable("POSTGRES_PASSWORD")
PG_ADDRESS  : str  = get_variable("POSTGRES_ADDRESS")
PG_NAME     : str  = get_variable("POSTGRES_NAME")
PG_PORT     : str  = get_variable("POSTGRES_PORT")
