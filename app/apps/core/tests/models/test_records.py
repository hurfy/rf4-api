from django.test      import TestCase

from apps.core.models import Record


class RecordModelTestCase(TestCase):
    def setUp(self) -> None:
        self.record = Record.objects.create(
            fish     = "Nelma",
            weight   = 23.653,
            location = "Lower Tunguska River",
            bait     = "Soturi 22g-009",
            player   = "hurfy",
            date     = "2024-02-18",
            region   = "cis",
            rec_type = "records"
        )

    def test_create_valid_data(self) -> None:
        self.assertEqual(self.record.fish, 'Nelma')
        self.assertEqual(self.record.weight, 23.653)
        self.assertEqual(self.record.location, 'Lower Tunguska River')
        self.assertEqual(self.record.bait, 'Soturi 22g-009')
        self.assertEqual(self.record.player, 'hurfy')
        self.assertEqual(self.record.date, '2024-02-18')
        self.assertEqual(self.record.region, 'cis')
        self.assertEqual(self.record.rec_type, 'records')

    def test_create_invalid_data(self) -> None:
        with self.assertRaises(Exception):
            Record.objects.create(
                fish     = True,
                weight   = "12.12",
                location = None,
                lure     = 34.1,
                player   = [],
                date     = {12, 24, 18},
                region   = lambda x: int(x)
            )

    def test_record_str_representation(self) -> None:
        expected_str = (
            f"Fish    : {self.record.fish}\n"
            f"Weight  : {self.record.weight}\n"
            f"Location: {self.record.location}\n"
            f"Bait    : {self.record.bait}\n"
            f"Player  : {self.record.player}\n"
            f"Date    : {self.record.date}\n"
            f"Region  : {self.record.region}\n"
            f"Type    : {self.record.rec_type}"
        )
        self.assertEqual(str(self.record), expected_str)

    def test_record_as_dict(self) -> None:
        expected_dict = {
            "fish"    : self.record.fish,
            "weight"  : self.record.weight,
            "location": self.record.location,
            "bait"    : self.record.bait,
            "player"  : self.record.player,
            "date"    : self.record.date,
            "region"  : self.record.region,
            "type"    : self.record.rec_type
        }
        self.assertEqual(self.record.as_dict, expected_dict)

    def test_record_weight_in_gram(self) -> None:
        # 23653g
        self.assertEqual(self.record.weight_in_gram, self.record.weight * 1000)