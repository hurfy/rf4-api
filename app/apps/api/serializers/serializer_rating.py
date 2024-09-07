from rest_framework         import serializers

from apps.core.models       import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Rating
        fields = ["position", "player", "level", "ingame", "region"]

    def to_representation(self, instance) -> dict:
        """
        If the query parameter "in_days" is set to "true", the in-game days attribute is converted from hours to days
        """
        data = super().to_representation(instance)

        if self.context.get("in_days") == "true":
            data["ingame"] = instance.ingame_in_days

        return data