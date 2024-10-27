from rest_framework.response import Response
from rest_framework.request  import Request
from rest_framework          import status, generics

from apps.api.serializers    import ParserSerializer
from apps.parser.tasks       import process_data


class ParserAPIView(generics.GenericAPIView):
    serializer_class = ParserSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        # Validate data
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get and initialize data
        categories = serializer.validated_data.get("categories")
        values     = {
            "abs_records": ("records", "AbsoluteRecord", False),
            "wk_records" : ("records", "WeeklyRecord", True),
            "ratings"    : ("ratings", "Rating", False),
            "winners"    : ("winners", "Winner", False),
        }
        tasks      = []

        # Parse all tables
        if "*" in categories:
            for each in values.values():
                task_category, model_name, weekly = each
                tasks.append(
                    {"id": process_data.delay(task_category, model_name, weekly=weekly).id, "status": "CREATED"}
                )

        else:
            for each in categories:
                task_category, model_name, weekly = values[each]
                tasks.append(
                    {"id": process_data.delay(task_category, model_name, weekly=weekly).id, "status": "CREATED"}
                )

        return Response({"tasks": tasks}, status=status.HTTP_200_OK)