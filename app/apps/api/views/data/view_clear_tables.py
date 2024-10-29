from rest_framework.response import Response
from rest_framework.request  import Request
from drf_spectacular.utils   import extend_schema
from rest_framework          import status, generics

from apps.api.serializers    import TablesListSerializer
from apps.core.models        import AbsoluteRecord, WeeklyRecord, Rating, Winner


@extend_schema(
    tags = ["DataProcessing"],
)
class ClearTablesAPIView(generics.GenericAPIView):
    serializer_class = TablesListSerializer
    # TODO: permissions

    def delete(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data = request.data)

        # Validate data
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # Get and initialize data
        tables = serializer.validated_data.get("tables")
        values = {
            "abs_records": AbsoluteRecord,
            "wk_records" : WeeklyRecord,
            "ratings"    : Rating,
            "winners"    : Winner,
        }

        # Clear all tables
        if "*" in tables:
            for each in values.values():
                each.objects.all().delete()

        # Clear individual tables
        else:
            for each in tables:
                values[each].objects.all().delete()

        return Response(status = status.HTTP_204_NO_CONTENT)