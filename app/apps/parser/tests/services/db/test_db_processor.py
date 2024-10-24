from django.db.models import QuerySet
from django.test import TestCase

from apps.parser.services import DBProcessor
from apps.core.models import AbsoluteRecord, WeeklyRecord, Rating, Winner


class DBProcessorTestCase(TestCase):
    @staticmethod
    def create_valid_records_data() -> list[dict]:
        return [
            {
                "fish"    : "Nelma",
                "weight"  : 23.653,
                "location": "Lower Tunguska River",
                "bait"    : "Soturi 22g-009",
                "player"  : "hurfy",
                "date"    : "2024-02-18",
                "region"  : "cis",
                "category": "records"
            },
            {
                "fish"    : "Albino barbel",
                "weight"  : 9.824,
                "location": " Bear Lake",
                "bait"    : "Cockchafer Larva",
                "player"  : "hurfy",
                "date"    : "2024-05-24",
                "region"  : "cis",
                "category": "records"
            },
        ]

    @staticmethod
    def create_invalid_records_data() -> list[dict]:
        return [
            {
                "fish"    : True,
                "weight"  : "12.12",
                "location": None,
                "lure"    : 34.1,
                "player"  : [],
                "date"    : {12, 24, 18},
                "region"  : lambda x: int(x),
                "category": {},
            }
        ]

    @staticmethod
    def create_valid_ratings_data() -> list[dict]:
        return [
            {
                "position": 12,
                "player"  : "hurfy123",
                "level"   : 34,
                "ingame"  : 1024,
                "region"  : "cis",
            },
            {
                "position": 1,
                "player"  : "hurfy",
                "level"   : 38,
                "ingame"  : 2048,
                "region"  : "en",
            }
        ]

    @staticmethod
    def create_invalid_ratings_data() -> list[dict]:
        return [
            {
                "position": -1,
                "player"  : None,
                "level"   : "hurfy",
                "ingame"  : True,
                "region"  : 12
            }
        ]

    @staticmethod
    def create_valid_winners_data() -> list[dict]:
        return [
            {
                "position": 1,
                "player"  : "hurfy",
                "records" : 3,
                "score"   : 10000,
                "prize"   : "",
                "region"  : "cis",
                "category": "records",
            },
            {
                "position": 12,
                "player"  : "hurfy123",
                "records" : 2,
                "score"   : 1212,
                "prize"   : "",
                "region"  : "en",
                "category": "ultralight",
            }
        ]

    @staticmethod
    def create_invalid_winners_data() -> list[dict]:
        return [
            {
                "position": "first",
                "records" : True,
                "score"   : 12.000,
                "player"  : ("hurfy",),
                "prize"   : [],
                "region"  : 123,
                "category": {},
            }
        ]

    def test_db_processor_records(self) -> None:
        # absolute
        DBProcessor.write("AbsoluteRecord", self.create_valid_records_data())

        data = AbsoluteRecord.objects.all()
        self.assertIsInstance(data, QuerySet), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)

        with self.assertRaises(Exception):
            DBProcessor.write("AbsoluteRecord", self.create_invalid_records_data())

        # weekly
        DBProcessor.write("WeeklyRecord", self.create_valid_records_data())

        data = WeeklyRecord.objects.all()
        self.assertIsInstance(data, QuerySet), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)

        with self.assertRaises(Exception):
            DBProcessor.write("WeeklyRecord", self.create_invalid_records_data())

    def test_db_processor_ratings(self) -> None:
        DBProcessor.write("Rating", self.create_valid_ratings_data())

        data = Rating.objects.all()
        self.assertIsInstance(data, QuerySet), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)

        with self.assertRaises(Exception):
            DBProcessor.write("Rating", self.create_invalid_ratings_data())

    def test_db_processor_winners(self) -> None:
        DBProcessor.write("Winner", self.create_valid_winners_data())

        data = Winner.objects.all()
        self.assertIsInstance(data, QuerySet), self.assertTrue(data), self.assertIsNotNone(data)
        self.assertEqual(len(data), 2)

        with self.assertRaises(Exception):
            DBProcessor.write("Winner", self.create_invalid_ratings_data())