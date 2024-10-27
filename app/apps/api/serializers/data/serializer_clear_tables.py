from rest_framework import serializers


class ClearTablesSerializer(serializers.Serializer):
    tables = serializers.ListField(
        child=serializers.CharField(max_length=24)
    )

    def validate_tables(self, value: list[str]) -> list[str]:
        error_text = ("Invalid value for 'tables' field. "
                      "Allowed values are: 'abs_records', 'wk_records', 'ratings', 'winners', '*'.")

        if not value:
            raise serializers.ValidationError(error_text)

        for each in value:
            if each not in ("abs_records", "wk_records", "ratings", "winners", "*"):
                raise serializers.ValidationError(error_text)

        return value