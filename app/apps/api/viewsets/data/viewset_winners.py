from rest_framework.exceptions import ValidationError
from rest_framework            import viewsets

from apps.api.serializers      import WinnerSerializer, URLParamsSerializer
from apps.api.paginators       import DefaultAPIPaginator
from apps.core.models          import Winner


class WinnerViewSet(viewsets.ModelViewSet):
    queryset         = Winner.objects.all()
    pagination_class = DefaultAPIPaginator
    serializer_class = WinnerSerializer
    ordering_fields  = "__all__"
    ordering         = ["position"]
    # TODO: permissions

    def get_queryset(self, *args, **kwargs) -> Winner:
        # Filtering against the URL
        region   = self.kwargs.get("region")
        category = self.kwargs.get("category")

        # Validate region
        serializer = URLParamsSerializer(
            data={
                "region": region,
            }
        )

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        return self.queryset.filter(region=region, category=category)