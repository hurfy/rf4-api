from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework        import viewsets
from django_filters        import rest_framework

from apps.api.serializers  import WinnerSerializer, URLParamsSerializer
from apps.core.paginators  import DefaultAPIPaginator
from apps.core.models      import Winner
from apps.core.filters     import WinnerFilter


@extend_schema_view(
    list           = extend_schema(tags = ["Winners"]),
    retrieve       = extend_schema(tags = ["Winners"]),
    create         = extend_schema(tags = ["Winners"]),
    update         = extend_schema(tags = ["Winners"]),
    partial_update = extend_schema(tags = ["Winners"]),
    destroy        = extend_schema(tags = ["Winners"]),
)
class WinnerViewSet(viewsets.ModelViewSet):
    queryset         = Winner.objects.all()
    pagination_class = DefaultAPIPaginator
    serializer_class = WinnerSerializer
    ordering_fields  = "__all__"
    ordering         = ["position"]
    filter_backends  = [rest_framework.DjangoFilterBackend]
    filterset_class  = WinnerFilter
    # TODO: permissions

    def get_queryset(self, *args, **kwargs) -> Winner:
        # Filtering against the URL
        region   = self.kwargs.get("region")
        category = self.kwargs.get("category")

        # Validate region
        URLParamsSerializer(
            data = {
                "region": region,
            }
        ).is_valid()

        return self.queryset.filter(region = region, category = category)