from django.test          import TestCase

from apps.parser.services import DBRatings
from apps.core.models     import Rating


class TestDBRatings(TestCase):
    def setUp(self) -> None:
        self.db_ratings = DBRatings()

        self.test_players_valid   = [
            {
                "position": 1,
                "player"  : "hurfy",
                "level"   : 10,
                "ingame"  : 100,
                "region"  : "gl"
            },
            {
                "position": 2,
                "player"  : "hurty",
                "level"   : 20,
                "ingame"  : 200,
                "region"  : "ru"
            },
        ]

        self.test_players_invalid = [
            {
                "position": -1,
                "player"  : None,
                "level"   : "test_level",
                "ingame"  : True,
                "region"  : 123
            },
        ]

    def test_create_valid_data(self) -> None:
        self.db_ratings.create(self.test_players_valid)
        self.assertEqual(Rating.objects.count(), 2)

    def test_create_invalid_data(self) -> None:
        with self.assertRaises(Exception):
            self.db_ratings.create(self.test_players_invalid)

    def test_serialize(self) -> None:
        serialized_ratings = self.db_ratings._serialize(self.test_players_valid)

        self.assertEqual(len(serialized_ratings), 2)
        self.assertIsInstance(serialized_ratings[0], Rating)