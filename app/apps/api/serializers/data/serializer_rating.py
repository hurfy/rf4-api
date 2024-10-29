from rest_framework   import serializers

from apps.core.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Rating
        fields = ["position", "player", "level", "ingame", "region"]

    def to_representation(self, instance: Rating) -> dict:
        data = super().to_representation(instance)

        # Ingame time in days
        if self.context.get("in_days") == "true":
            data["ingame"] = instance.ingame_in_days

        return data