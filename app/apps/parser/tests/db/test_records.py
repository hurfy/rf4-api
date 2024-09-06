from django.test          import TestCase

from apps.parser.services import DBRecords
from apps.core.models     import Record


class TestDBRecords(TestCase):
    def setUp(self) -> None:
        self.db_records = DBRecords()

        self.test_records_valid   = {
            "fish1": [
                {
                    "weight"  : 10.0,
                    "location": "river",
                    "bait"    : "snake",
                    "player"  : "hurfy",
                    "date"    : "2024-01-01",
                    "region"  : "gl",
                    "type"    : "ultralight"
                },
            ],
            "fish2": [
                {
                    "weight"  : 20.0,
                    "location": "river",
                    "bait"    : "snake",
                    "player"  : "hurty",
                    "date"    : "2024-01-01",
                    "region"  : "ru",
                    "type"    : "records",
                }
            ],
        }

        self.test_records_invalid = {
            1: [
                {
                    "weight"  : "river",
                    "location": True,
                    "bait"    : 12,
                    "player"  : False,
                    "date"    : "2024-0101",
                    "region"  : "helloworldhello",
                    "type"    : {1, 2, 3},
                }
            ]
        }

    def test_create_valid_data(self) -> None:
        self.db_records.create(self.test_records_valid)
        self.assertEqual(Record.objects.count(), 2)

    def test_create_invalid_data(self) -> None:
        with self.assertRaises(Exception):
            self.db_records.create(self.test_records_invalid)

    def test_serialize(self) -> None:
        serialized_ratings = self.db_records._serialize(self.test_records_valid)

        self.assertEqual(len(serialized_ratings), 2)
        self.assertIsInstance(serialized_ratings[0], Record)
