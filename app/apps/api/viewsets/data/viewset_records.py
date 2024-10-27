from rest_framework.exceptions import ValidationError
from rest_framework            import viewsets


from apps.api.serializers      import AbsoluteRecordSerializer, WeeklyRecordSerializer, URLParamsSerializer
from apps.api.paginators       import DefaultAPIPaginator
from apps.core.models          import Record, AbsoluteRecord, WeeklyRecord


class BaseRecordViewSet(viewsets.ModelViewSet):
    ordering_fields  = "__all__"
    ordering         = ["fish"]
    pagination_class = DefaultAPIPaginator
    # TODO: permissions

    def get_queryset(self, *args, **kwargs) -> Record:
        # Filtering against the URL
        region   = self.kwargs.get("region")
        category = self.kwargs.get("category")

        # Validate region
        URLParamsSerializer(
            data = {
                "region"  : region,
                "category": category,
            }
        ).is_valid()

        return self.queryset.filter(region = region, category = category)

    def get_serializer_context(self) -> dict:
        # Output the weight in grams or not?
        context = super().get_serializer_context()
        context.update(
            {
                "in_gram": self.request.GET.get("in_gram", "false"),
            }
        )

        return context


class AbsoluteRecordsViewSet(BaseRecordViewSet):
    queryset         = AbsoluteRecord.objects.all()
    serializer_class = AbsoluteRecordSerializer


class WeeklyRecordsViewSet(BaseRecordViewSet):
    queryset         = WeeklyRecord.objects.all()
    serializer_class = WeeklyRecordSerializer
