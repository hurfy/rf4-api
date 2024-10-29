from rest_framework import serializers


class TablesListSerializer(serializers.Serializer):
    allowed_values = ("abs_records", "wk_records", "ratings", "winners", "*")
    tables         = serializers.ListField(
        child = serializers.CharField(max_length = 24),
    )

    def validate_tables(self, values: list[str]) -> list[str]:
        error_text = (
            "Invalid value: '{}'. "
            f"Allowed values are: {self.allowed_values}."
        )

        # Empty
        if not values:
            raise serializers.ValidationError("The table list is empty.")

        # Validation of each item in the list
        for each in values:
            if each not in self.allowed_values:
                raise serializers.ValidationError(error_text.format(each))

        return values