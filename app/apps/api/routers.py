from rest_framework.routers import DefaultRouter

from apps.api.viewsets      import AbsoluteRecordsViewSet, WeeklyRecordsViewSet, RatingViewSet, WinnerViewSet


records_router = DefaultRouter()
records_router.register(r"abs/(?P<region>\w+)/(?P<category>\w+)", AbsoluteRecordsViewSet, basename="AbsoluteRecords")
records_router.register(r"wk/(?P<region>\w+)/(?P<category>\w+)",  WeeklyRecordsViewSet,   basename="WeeklyRecords")

ratings_router = DefaultRouter()
ratings_router.register(r"(?P<region>\w+)", RatingViewSet, basename="Ratings")

winners_router = DefaultRouter()
winners_router.register(r"(?P<region>\w+)/(?P<category>\w+)", WinnerViewSet, basename="Winners")