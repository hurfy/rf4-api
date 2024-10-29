from rest_framework import serializers
from django.http    import Http404


class URLParamsSerializer(serializers.Serializer):
    region   = serializers.CharField(max_length = 24)
    category = serializers.CharField(max_length = 24, required = False)

    def validate_region(self, value: str) -> str:
        return self._in_list(value, ("gl", "ru", "de", "us", "fr", "cn", "pl", "kr", "jp", "en"))

    def validate_category(self, value: str) -> str:
        return self._in_list(value, ("records", "ultralight", "telestick"))

    @staticmethod
    def _in_list(value: str, _list: list[str] or tuple) -> str:
        if value not in _list:
            raise Http404

        return value