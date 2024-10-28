from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework        import viewsets
from django_filters        import rest_framework

from apps.api.serializers  import RatingSerializer, URLParamsSerializer
from apps.api.paginators   import DefaultAPIPaginator
from apps.core.models      import Rating
from apps.core.filters     import RatingFilter


@extend_schema_view(
    list=extend_schema(tags=["Ratings"]),
    retrieve=extend_schema(tags=["Ratings"]),
    create=extend_schema(tags=["Ratings"]),
    update=extend_schema(tags=["Ratings"]),
    partial_update=extend_schema(tags=["Ratings"]),
    destroy=extend_schema(tags=["Ratings"]),
)
class RatingViewSet(viewsets.ModelViewSet):
    queryset         = Rating.objects.all()
    pagination_class = DefaultAPIPaginator
    serializer_class = RatingSerializer
    ordering_fields  = "__all__"
    ordering         = ["position"]
    filter_backends  = [rest_framework.DjangoFilterBackend]
    filterset_class  = RatingFilter
    # TODO: permissions

    def get_queryset(self, *args, **kwargs) -> Rating:
        # Filtering against the URL
        region = self.kwargs.get("region")

        # Validate region
        URLParamsSerializer(
            data = {
                "region": region,
            }
        ).is_valid()

        return self.queryset.filter(region = region)

    def get_serializer_context(self) -> dict:
        # Output the gametime in days or not?
        context = super().get_serializer_context()
        context.update(
            {
                "region" : self.kwargs.get("region"),
                "in_days": self.request.GET.get("in_days", "false"),
            }
        )

        return context