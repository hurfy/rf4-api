from django.urls    import path

from apps.api.views import RecordsAPIView, RatingsAPIView, ParserAPIView

urlpatterns = [
    path("records/<str:category>/<str:region>/", RecordsAPIView.as_view()),
    path("ratings/<str:region>/",            RatingsAPIView.as_view()),
    # Parse data
    path("parse/", ParserAPIView.as_view()),
]