from django.test      import TestCase

from apps.core.models import Record, AbsoluteRecord, WeeklyRecord


class BaseRecordModelTestCase(TestCase):
    model = Record

    def create_valid_data(self) -> Record:
        return self.model.objects.create(
            fish     = "Nelma",
            weight   = 23.653,
            location = "Lower Tunguska River",
            bait     = "Soturi 22g-009",
            player   = "hurfy",
            date     = "2024-02-18",
            region   = "cis",
            category = "records"
        )

    def create_invalid_data(self) -> Record:
        return self.model.objects.create(
                fish     = True,
                weight   = "12.12",
                location = None,
                lure     = 34.1,
                player   = [],
                date     = {12, 24, 18},
                region   = lambda x: int(x),
                category = {},
            )

    def setUp(self) -> None:
        self.data = self.create_valid_data()

    def test_create_valid(self) -> None:
        self.assertIsInstance(self.data, Record), self.assertTrue(self.data), self.assertIsNotNone(self.data)

        self.assertEqual(self.data.fish, 'Nelma')
        self.assertEqual(self.data.weight, 23.653)
        self.assertEqual(self.data.location, 'Lower Tunguska River')
        self.assertEqual(self.data.bait, 'Soturi 22g-009')
        self.assertEqual(self.data.player, 'hurfy')
        self.assertEqual(self.data.date, '2024-02-18')
        self.assertEqual(self.data.region, 'cis')
        self.assertEqual(self.data.category, 'records')

    def test_create_invalid(self) -> None:
        with self.assertRaises(Exception):
            self.create_invalid_data()

    def test_as_str(self) -> None:
        expected_data = (
            f"Fish    : Nelma\n"
            f"Weight  : 23.653\n"
            f"Location: Lower Tunguska River\n"
            f"Bait    : Soturi 22g-009\n"
            f"Player  : hurfy\n"
            f"Date    : 2024-02-18\n"
            f"Region  : cis\n"
            f"Category: records"
        )

        self.assertEqual(str(self.data), expected_data)

    def test_as_dict(self) -> None:
        expected_data = {
            "fish"    : "Nelma",
            "weight"  : 23.653,
            "location": "Lower Tunguska River",
            "bait"    : "Soturi 22g-009",
            "player"  : "hurfy",
            "date"    : "2024-02-18",
            "region"  : "cis",
            "category": "records"
        }
        self.assertEqual(self.data.as_dict, expected_data)

    def test_weight_in_gram(self) -> None:
        self.assertEqual(self.data.weight_in_gram, self.data.weight * 1000)  # 23653g


class AbsoluteRecordTestCase(BaseRecordModelTestCase):
    model = AbsoluteRecord


class WeeklyRecordTestCase(BaseRecordModelTestCase):
    model = WeeklyRecord
