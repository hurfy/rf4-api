from django.test      import TestCase

from apps.core.models import Winner


class WinnerModelTestCase(TestCase):
    @staticmethod
    def create_valid_data() -> Winner:
        return Winner.objects.create(
            position = 1,
            records  = 3,
            score    = 10000,
            player   = "hurfy",
            prize    = "",
            region   = "cis",
            category = "records",
        )

    @staticmethod
    def create_invalid_data() -> Winner:
        return Winner.objects.create(
            position = "first",
            records  = True,
            score    = 12.000,
            player   = ("hurfy",),
            prize    = [],
            region   = 123,
            category = {},
        )

    def setUp(self) -> None:
        self.data = self.create_valid_data()

    def test_create_valid(self) -> None:
        self.assertIsInstance(self.data, Winner), self.assertTrue(self.data), self.assertIsNotNone(self.data)

        self.assertEqual(self.data.position, 1)
        self.assertEqual(self.data.records, 3)
        self.assertEqual(self.data.score, 10000)
        self.assertEqual(self.data.player, "hurfy")
        self.assertEqual(self.data.prize, "")

    def test_create_invalid(self) -> None:
        with self.assertRaises(Exception):
            self.create_invalid_data()

    def test_as_str(self) -> None:
        expected_data = (
            f"Position: 1\n"
            f"Player  : hurfy\n"
            f"Records : 3\n"
            f"Score   : 10000\n"
            f"Prize   : \n"
            f"Region  : cis\n"
            f"Category: records"
        )

        self.assertEqual(str(self.data), expected_data)

    def test_as_dict(self) -> None:
        expected_data = {
            "position": 1,
            "player"  : "hurfy",
            "records" : 3,
            "score"   : 10000,
            "prize"   : "",
            "region"  : "cis",
            "category": "records",
        }

        self.assertEqual(self.data.as_dict, expected_data)
