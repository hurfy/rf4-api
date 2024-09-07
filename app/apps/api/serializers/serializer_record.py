from rest_framework         import serializers

from apps.core.models       import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Record
        fields = ["fish", "weight", "location", "bait", "player", "date", "region", "rec_type"]

    def to_representation(self, instance) -> dict:
        """
        If the `in_gram` parameter is set to `"true"` in the context, the `weight` field will be represented in grams
        """
        data = super().to_representation(instance)

        if self.context.get("in_gram") == "true":
            data["weight"] = instance.weight_in_gram

        return data