from django.urls            import path, include

from apps.api.views         import ParserAPIView, ClearTablesAPIView
from apps.api.routers       import records_router, ratings_router, winners_router


urlpatterns = [
    # Parse data
    path("parse/", ParserAPIView.as_view()),
    # Clear tables
    path("clear/", ClearTablesAPIView.as_view()),
    # Tables
    path("records/", include(records_router.urls)),
    path("ratings/", include(ratings_router.urls)),
    path("winners/", include(winners_router.urls)),
]