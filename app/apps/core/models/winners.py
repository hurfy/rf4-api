from django.db import models


class Winner(models.Model):
    position = models.PositiveIntegerField(verbose_name="Rating position")
    records  = models.PositiveIntegerField(verbose_name="Records count")
    score    = models.PositiveIntegerField(verbose_name="Score")
    player   = models.CharField(verbose_name="Username", max_length=256)
    prize    = models.CharField(verbose_name="Prize", max_length=256, blank=True)

    class Meta:
        verbose_name = "Winner"
        db_table     = "core_winners"
        ordering     = ["id"]

    def __str__(self) -> str:
        return (
            f"Position: {self.position}\n"
            f"Player  : {self.player}\n"
            f"Records : {self.records}\n"
            f"Score   : {self.score}\n"
            f"Prize   : {self.prize}"
        )

    @property
    def as_dict(self) -> dict:
        return {
            "position": self.position,
            "player"  : self.player,
            "records" : self.records,
            "score"   : self.score,
            "prize"   : self.prize,
        }