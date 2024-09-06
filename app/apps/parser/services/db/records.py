from django.db        import transaction

from apps.core.models import Record


# TODO: Perhaps should make a base class to avoid code duplication
class DBRecords:
    def create(self, records: dict) -> None:
        # We guarantee that both requests will succeed, otherwise neither of them will be executed
        with transaction.atomic():
            Record.objects.all().delete()
            Record.objects.bulk_create(
                self._serialize(records)
            )

    @staticmethod
    def _serialize(records: dict) -> list[Record]:
        records_list = []

        for fish in records:
            for record in records[fish]:
                records_list.append(
                    Record(
                        fish     = fish,
                        weight   = record.get("weight", 0),
                        location = record.get("location", ""),
                        bait     = record.get("bait", ""),
                        player   = record.get("username", ""),
                        date     = record.get("date", ""),
                        region   = record.get("region", ""),
                        rec_type = record.get("type", ""),
                    )
                )

        return records_list
