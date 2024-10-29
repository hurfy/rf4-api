from rest_framework   import serializers

from apps.core.models import Winner


class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Winner
        fields = ["position", "records", "score", "player", "prize", "region", "category"]