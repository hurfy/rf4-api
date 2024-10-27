from rest_framework import serializers


class ParserSerializer(serializers.Serializer):
    categories = serializers.ListField(
        child = serializers.CharField(max_length=24)
    )

    def validate_categories(self, value: list[str]) -> list[str]:
        error_text = ("Invalid value for 'categories' field. "
                      "Allowed values are: 'abs_records', 'wk_records', 'ratings', 'winners', '*'.")

        if not value:
            raise serializers.ValidationError(error_text)

        for each in value:
            if each not in ("abs_records", "wk_records", "ratings", "winners", "*"):
                raise serializers.ValidationError(error_text)

        return value
