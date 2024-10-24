from rest_framework.response import Response
from rest_framework.request  import Request
from rest_framework          import status, generics

from apps.api.serializers    import ParserSerializer
from apps.parser.tasks       import process_data


class ParserAPIView(generics.GenericAPIView):
    serializer_class = ParserSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        category = serializer.validated_data.get("category")
        weekly   = serializer.validated_data.get("weekly", False)

        if category not in ("records", "ratings", "winners", "all"):
            return Response(
                {"error": f"Invalid category: {category}. Allowed values are [records, ratings, winners, all]."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        def run_task(task_category, model_name: str) -> dict:
            return {"id": process_data.delay(task_category, model_name).id, "status": "CREATED"}

        category_tasks = {
            "records": lambda: run_task("records", "WeeklyRecord" if weekly else "AbsoluteRecord"),
            "ratings": lambda: run_task("ratings", "Rating"),
            "winners": lambda: run_task("winners", "Winner"),
            "all"    : lambda: [
                run_task("records", "AbsoluteRecord"),
                run_task("records", "WeeklyRecord"),
                run_task("ratings", "Rating"),
                run_task("winners", "Winner"),
            ]
        }

        if category == "all":
            return Response({"tasks": category_tasks[category]()}, status=status.HTTP_200_OK)

        return Response(category_tasks[category](), status=status.HTTP_200_OK)