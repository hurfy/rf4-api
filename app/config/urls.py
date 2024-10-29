from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib        import admin
from django.urls           import path, include

urlpatterns = [
    # API
    path("", include("apps.api.urls")),
    # Stuff
    path("admin/", admin.site.urls),
    # Open API
    path("docs/",         SpectacularAPIView.as_view(), name="schema"),
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("docs/redoc/",   SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
