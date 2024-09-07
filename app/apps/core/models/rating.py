from django.db import models


class Rating(models.Model):
    position = models.PositiveIntegerField(verbose_name="Rating position")
    player   = models.CharField(verbose_name="Username", max_length=256)
    level    = models.PositiveIntegerField(verbose_name="Player level")
    ingame   = models.PositiveIntegerField(verbose_name="In-game days")
    region   = models.CharField(verbose_name="Rating region", max_length=4)

    class Meta:
        verbose_name = "Rating"
        db_table     = "core_rating"
        ordering     = ["id"]

    def __str__(self) -> str:
        return (
            f"Position: {self.position}\n"
            f"Player  : {self.player}\n"
            f"Level   : {self.level}\n"
            f"InGame  : {self.ingame}\n"
            f"Region  : {self.region}"
        )

    @property
    def as_dict(self) -> dict:
        return {
            "position": self.position,
            "player"  : self.player,
            "level"   : self.level,
            "ingame"  : self.ingame,
            "region"  : self.region,
        }

    @property
    def ingame_in_days(self) -> float:
        return round(self.ingame / 24, 2)