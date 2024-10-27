from django_filters   import rest_framework as filters

from apps.core.models import AbsoluteRecord, WeeklyRecord


class RecordFilter(filters.FilterSet):
    weight     = filters.NumberFilter(field_name="weight")
    max_weight = filters.NumberFilter(field_name="weight", lookup_expr="lte")
    min_weight = filters.NumberFilter(field_name="weight", lookup_expr="gte")

    fish     = filters.CharFilter(field_name="fish")
    location = filters.CharFilter(field_name="location")
    bait     = filters.CharFilter(field_name="bait")  # Has bait filter maybe???
    player   = filters.CharFilter(field_name="player")

    date        = filters.DateFilter(label='date')  # Hate 'dis
    date_after  = filters.DateFilter(field_name="date", lookup_expr='gte')
    date_before = filters.DateFilter(field_name="date", lookup_expr='lte')


class AbsoluteRecordFilter(RecordFilter):
    class Meta:
        model  = AbsoluteRecord
        fields = ["weight", "max_weight", "min_weight", "fish", "location", "bait", "player", "date", "date_after",
                  "date_before"]


class WeeklyRecordFilter(RecordFilter):
    class Meta:
        model  = WeeklyRecord
        fields = ["weight", "max_weight", "min_weight", "fish", "location", "bait", "player", "date", "date_after",
                  "date_before"]
