from django.urls      import path, include

from apps.api.views   import ParserAPIView, ClearTablesAPIView
from apps.api.routers import records_router, ratings_router, winners_router


urlpatterns = [
    # Parse data
    path("v1/parse/", ParserAPIView.as_view()),
    # Clear tables
    path("v1/clear/", ClearTablesAPIView.as_view()),
    # Tables
    path("v1/records/", include(records_router.urls)),
    path("v1/ratings/", include(ratings_router.urls)),
    path("v1/winners/", include(winners_router.urls)),
]