from django.db.models import QuerySet
from django_filters   import rest_framework as filters

from apps.core.models import Winner


class WinnerFilter(filters.FilterSet):
    position     = filters.NumberFilter(field_name="position")
    max_position = filters.filters.NumberFilter(field_name="position", lookup_expr="lte")
    min_position = filters.filters.NumberFilter(field_name="position", lookup_expr="gte")

    records     = filters.NumberFilter(field_name="records")
    max_records = filters.NumberFilter(field_name="records", lookup_expr="lte")
    min_records = filters.NumberFilter(field_name="records", lookup_expr="gte")

    score     = filters.NumberFilter(field_name="score")
    max_score = filters.NumberFilter(field_name="score", lookup_expr="lte")
    min_score = filters.NumberFilter(field_name="score", lookup_expr="gte")

    player = filters.CharFilter(field_name="player")

    prize     = filters.CharFilter(field_name="prize")
    has_prize = filters.BooleanFilter(field_name="prize", method="filter_has_prize")

    def filter_has_prize(self, queryset: QuerySet, name, value: str) -> QuerySet:
        return queryset.filter(prize__isnull=False) if value else queryset.filter(prize__isnull=True)

    class Meta:
        model  = Winner
        fields = ["position", "max_position", "min_position", "records", "max_records", "min_records", "score",
                  "max_score", "min_score", "player", "prize", "has_prize"]
