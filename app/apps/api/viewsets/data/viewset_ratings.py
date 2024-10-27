from rest_framework.exceptions import ValidationError
from rest_framework            import viewsets

from apps.api.serializers      import RatingSerializer, URLParamsSerializer
from apps.api.paginators       import DefaultAPIPaginator
from apps.core.models          import Rating


class RatingViewSet(viewsets.ModelViewSet):
    queryset         = Rating.objects.all()
    pagination_class = DefaultAPIPaginator
    serializer_class = RatingSerializer
    ordering_fields  = "__all__"
    ordering         = ["position"]
    # TODO: permissions

    def get_queryset(self, *args, **kwargs) -> Rating:
        # Filtering against the URL
        region = self.kwargs.get("region")

        # Validate region
        serializer = URLParamsSerializer(
            data = {
                "region": region,
            }
        )

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

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