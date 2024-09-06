from django.db import models


class Record(models.Model):
    fish     = models.CharField(verbose_name="Fish name", max_length=64)
    weight   = models.DecimalField(verbose_name="Fish weight", max_digits=16, decimal_places=3)
    location = models.CharField(verbose_name="Location", max_length=64)
    bait     = models.CharField(verbose_name="Bait name", max_length=128)
    player   = models.CharField(verbose_name="Username", max_length=256)
    date     = models.DateField(verbose_name="Date of catch")
    region   = models.CharField(verbose_name="Record region", max_length=4)
    rec_type = models.CharField(verbose_name="Record type", max_length=16)

    class Meta:
        verbose_name = "Record"
        db_table     = "core_records"
        ordering     = ["id"]

    def __str__(self) -> str:
        return (
            f"Fish    : {self.fish}\n"
            f"Weight  : {self.weight}\n"
            f"Location: {self.location}\n"
            f"Bait    : {self.bait}\n"
            f"Player  : {self.player}\n"
            f"Date    : {self.date}\n"
            f"Region  : {self.region}\n"
            f"Type    : {self.rec_type}"
        )

    @property
    def as_dict(self) -> dict:
        return {
            "fish"    : self.fish,
            "weight"  : self.weight,
            "location": self.location,
            "bait"    : self.bait,
            "player"  : self.player,
            "date"    : self.date,
            "region"  : self.region,
            "type"    : self.rec_type,
        }

    @property
    def weight_in_gram(self) -> int:
        return int(self.weight * 1000)
