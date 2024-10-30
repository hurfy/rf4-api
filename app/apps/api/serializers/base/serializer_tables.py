from rest_framework import serializers


class TablesListSerializer(serializers.Serializer):
    tables = serializers.ListField(
        child       = serializers.CharField(max_length = 24),
        allow_empty = False,
        max_length  = 5,
    )

    def validate_tables(self, values: list[str]) -> list[str]:
        allowed_values = ("abs_records", "wk_records", "ratings", "winners", "*")
        error_text     = (
            "Invalid value: '{}'. "
            f"Allowed values are: {allowed_values}."
        )

        # Validation of each item in the list
        for each in values:
            if each not in allowed_values:
                raise serializers.ValidationError(error_text.format(each))

        return values