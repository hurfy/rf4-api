from rest_framework import serializers


class ParserSerializer(serializers.Serializer):
    category = serializers.CharField()
    weekly   = serializers.BooleanField(required=False)
