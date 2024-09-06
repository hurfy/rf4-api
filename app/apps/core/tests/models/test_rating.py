from django.test      import TestCase

from apps.core.models import Rating


class RatingModelTestCase(TestCase):
    def setUp(self) -> None:
        self.rating = Rating.objects.create(
            position = 12,
            player   = "hurfy",
            level    = 34,
            ingame   = 1024,
            region   = "CIS"
        )

    def test_create_valid_data(self) -> None:
        self.assertEquals(self.rating.position, 12)
        self.assertEquals(self.rating.player, "hurfy")
        self.assertEquals(self.rating.level, 34)
        self.assertEquals(self.rating.ingame, 1024)
        self.assertEquals(self.rating.region, "CIS")

    def test_create_invalid_data(self) -> None:
        with self.assertRaises(Exception):
            Rating.objects.create(
                position = -1,
                player   = None,
                level    = "hurfy",
                ingame   = True,
                region   = 12
            )

    def test_rating_str_representation(self) -> None:
        expected_str = (
                f"Position: {self.rating.position}\n"
                f"Player  : {self.rating.player}\n"
                f"Level   : {self.rating.level}\n"
                f"InGame  : {self.rating.ingame}\n"
                f"Region  : {self.rating.region}"
        )
        self.assertEqual(str(self.rating), expected_str)

    def test_rating_as_dict(self) -> None:
        expected_dict = {
            "position": self.rating.position,
            "player"  : self.rating.player,
            "level"   : self.rating.level,
            "ingame"  : self.rating.ingame,
            "region"  : self.rating.region
        }
        self.assertEquals(self.rating.as_dict, expected_dict)

    def test_rating_ingame_in_hours(self) -> None:
        # 42.66h
        self.assertEquals(self.rating.ingame_in_hours, round(self.rating.ingame / 24, 2))