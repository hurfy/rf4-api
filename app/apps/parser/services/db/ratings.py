from django.db        import transaction

from apps.core.models import Rating


# TODO: Perhaps should make a base class to avoid code duplication
class DBRatings:
    def create(self, ratings: list[dict]) -> None:
        # We guarantee that both requests will succeed, otherwise neither of them will be executed
        with transaction.atomic():
            Rating.objects.all().delete()
            Rating.objects.bulk_create(
                self._serialize(ratings)
            )

    @staticmethod
    def _serialize(ratings: list[dict]) -> list[Rating]:
        ratings_list = []

        for rating in ratings:
            ratings_list.append(
                Rating(
                    position = rating.get("position", 0),
                    player   = rating.get("username", ""),
                    level    = rating.get("level", 0),
                    ingame   = rating.get("gametime", 0),
                    region   = rating.get("region", "")
                )
            )

        return ratings_list