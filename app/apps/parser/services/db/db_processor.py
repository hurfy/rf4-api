from django.apps import apps
from django.db   import transaction


class DBProcessor:
    @staticmethod
    @transaction.atomic()
    def write(model_name: str, data: list[dict]) -> None:
        """Updating the database with new data"""
        model = apps.get_model(f"core.{model_name}")

        model.objects.all().delete()
        model.objects.bulk_create(
            [model(**each) for each in data]
        )