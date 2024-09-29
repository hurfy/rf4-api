from django.test      import TestCase

from apps.core.models import Rating


class RatingModelTestCase(TestCase):
    @staticmethod
    def create_valid_data() -> Rating:
        return Rating.objects.create(
            position = 12,
            player   = "hurfy",
            level    = 34,
            ingame   = 1024,
            region   = "CIS"
        )

    @staticmethod
    def create_invalid_data() -> Rating:
        return Rating.objects.create(
                position = -1,
                player   = None,
                level    = "hurfy",
                ingame   = True,
                region   = 12
            )

    def setUp(self) -> None:
        self.data = self.create_valid_data()

    def test_create_valid(self) -> None:
        self.assertIsInstance(self.data, Rating), self.assertTrue(self.data), self.assertIsNotNone(self.data)

        self.assertEquals(self.data.position, 12)
        self.assertEquals(self.data.player, "hurfy")
        self.assertEquals(self.data.level, 34)
        self.assertEquals(self.data.ingame, 1024)
        self.assertEquals(self.data.region, "CIS")

    def test_create_invalid(self) -> None:
        with self.assertRaises(Exception):
            self.create_invalid_data()

    def test_rating_str_representation(self) -> None:
        expected_data = (
                f"Position: 12\n"
                f"Player  : hurfy\n"
                f"Level   : 34\n"
                f"InGame  : 1024\n"
                f"Region  : CIS"
        )
        self.assertEqual(str(self.data), expected_data)

    def test_rating_as_dict(self) -> None:
        expected_data = {
            "position": 12,
            "player"  : "hurfy",
            "level"   : 34,
            "ingame"  : 1024,
            "region"  : "CIS",
        }
        self.assertEquals(self.data.as_dict, expected_data)

    def test_rating_ingame_in_hours(self) -> None:
        self.assertEquals(self.data.ingame_in_days, round(self.data.ingame / 24, 2))  # 42.66h