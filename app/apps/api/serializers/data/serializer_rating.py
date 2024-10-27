from rest_framework         import serializers

from apps.core.models       import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Rating
        fields = ["position", "player", "level", "ingame", "region"]

    def validate(self, attrs):
        region     = self.context.get("region")
        error_text = ("Invalid value for region in URL."
                      "Allowed values are: 'gl', 'ru', 'de', 'us', 'fr', 'cn', 'pl', 'kr', 'jp', 'en'.")

        if region not in ("gl", "ru", "de", "us", "fr", "cn", "pl", "kr", "jp", "en"):
            raise serializers.ValidationError(error_text)

    def to_representation(self, instance) -> dict:
        """
        If the query parameter "in_days" is set to "true", the in-game days attribute is converted from hours to days
        """
        data = super().to_representation(instance)

        if self.context.get("in_days") == "true":
            data["ingame"] = instance.ingame_in_days

        return data