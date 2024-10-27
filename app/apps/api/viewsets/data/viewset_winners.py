from rest_framework       import viewsets
from django_filters       import rest_framework

from apps.api.serializers import WinnerSerializer, URLParamsSerializer
from apps.api.paginators  import DefaultAPIPaginator
from apps.core.models     import Winner
from apps.core.filters    import WinnerFilter


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
            data={
                "region": region,
            }
        ).is_valid()

        return self.queryset.filter(region=region, category=category)