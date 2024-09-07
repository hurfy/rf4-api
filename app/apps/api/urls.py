from django.urls    import path

from apps.api.views import RecordsAPIView, RatingsAPIView

urlpatterns = [
    path("records/<str:type>/<str:region>/", RecordsAPIView.as_view()),
    path("ratings/<str:region>/",            RatingsAPIView.as_view())
]