from django.http import Http404
from rest_framework import serializers


class URLParamsSerializer(serializers.Serializer):
    region   = serializers.CharField(max_length=24)
    category = serializers.CharField(max_length=24, required=False)

    def validate_region(self, value: str) -> str:
        if value not in ("gl", "ru", "de", "us", "fr", "cn", "pl", "kr", "jp", "en"):
            raise Http404

        return value

    def validate_category(self, value: str) -> str:
        if value not in ("records", "ultralight", "telestick"):
            raise Http404

        return value