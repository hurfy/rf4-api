from rest_framework         import serializers

from apps.core.models       import AbsoluteRecord, WeeklyRecord


class BaseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["fish", "weight", "location", "bait", "player", "date", "region", "category"]

    def to_representation(self, instance) -> dict:
        """
        If the `in_gram` parameter is set to `"true"` in the context, the `weight` field will be represented in grams.
        """
        data = super().to_representation(instance)

        if self.context.get("in_gram") == "true":
            data["weight"] = instance.weight_in_gram

        return data


class AbsoluteRecordSerializer(BaseRecordSerializer):
    class Meta(BaseRecordSerializer.Meta):
        model = AbsoluteRecord


class WeeklyRecordSerializer(BaseRecordSerializer):
    class Meta(BaseRecordSerializer.Meta):
        model = WeeklyRecord