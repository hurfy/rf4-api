from rest_framework.response import Response
from rest_framework.request  import Request
from drf_spectacular.utils   import extend_schema
from rest_framework          import status, generics

from apps.api.serializers    import TablesListSerializer
from apps.parser.tasks       import process_data


@extend_schema(
    tags = ["DataProcessing"],
)
class ParserAPIView(generics.GenericAPIView):
    serializer_class = TablesListSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data = request.data)

        # Validate data
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # Get and initialize data
        tables = serializer.validated_data.get("tables")
        values = {
            "abs_records": ("records", "AbsoluteRecord", False),
            "wk_records" : ("records", "WeeklyRecord", True),
            "ratings"    : ("ratings", "Rating", False),
            "winners"    : ("winners", "Winner", False),
        }
        tasks      = []

        # Parse all tables
        if "*" in tables:
            for each in values.values():
                task_category, model_name, weekly = each
                tasks.append(
                    {"id": process_data.delay(task_category, model_name, weekly = weekly).id, "status": "CREATED"}
                )

        else:
            for each in tables:
                task_category, model_name, weekly = values[each]
                tasks.append(
                    {"id": process_data.delay(task_category, model_name, weekly = weekly).id, "status": "CREATED"}
                )

        return Response({"tasks": tasks}, status = status.HTTP_200_OK)
