from django_filters   import rest_framework as filters

from apps.core.models import Rating


class RatingFilter(filters.FilterSet):
    position     = filters.NumberFilter(field_name="position")
    max_position = filters.filters.NumberFilter(field_name="position", lookup_expr="lte")
    min_position = filters.filters.NumberFilter(field_name="position", lookup_expr="gte")

    level     = filters.NumberFilter(field_name="level")
    max_level = filters.NumberFilter(field_name="level", lookup_expr="lte")
    min_level = filters.NumberFilter(field_name="level", lookup_expr="gte")

    ingame     = filters.NumberFilter(field_name="ingame")
    max_ingame = filters.NumberFilter(field_name="ingame", lookup_expr="lte")
    min_ingame = filters.NumberFilter(field_name="ingame", lookup_expr="gte")

    player = filters.CharFilter(field_name="player")

    class Meta:
        model  = Rating
        fields = ["position", "max_position", "min_position", "level", "max_level", "min_level", "ingame", "max_ingame",
                  "min_ingame", "player"]
