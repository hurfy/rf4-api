from django.db import models


class Rating(models.Model):
    fish     = models.CharField(max_length=255)
    weight   = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    lure     = models.CharField(max_length=255, null=True, blank=True)
    player   = models.CharField(max_length=255, null=True, blank=True)
    date     = models.DateField(null=True, blank=True)

    class Meta:
        abstract     = True
        verbose_name = "Rating"
        ordering     = ["id"]

    def __str__(self) -> str:
        return (
            f"Fish    : {self.fish}\n"
            f"Weight  : {self.weight}\n"
            f"Location: {self.location}\n"
            f"Lure    : {self.lure}\n"
            f"Player  : {self.player}\n"
            f"Date    : {self.date}"
        )

    @property
    def as_dict(self) -> dict:
        return {
            "fish"    : self.fish,
            "weight"  : self.weight,
            "location": self.location,
            "lure"    : self.lure,
            "player"  : self.player,
            "date"    : self.date
        }

