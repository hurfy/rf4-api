from rest_framework          import generics
from django.http             import Http404

from apps.api.serializers    import RatingSerializer
from apps.parser.services    import URLsManager
from apps.api.paginators     import DefaultAPIPaginator
from apps.core.models        import Rating


class RatingsAPIView(generics.ListAPIView):
    serializer_class = RatingSerializer
    pagination_class = DefaultAPIPaginator

    def get_queryset(self) -> Rating:
        """
        The region parameter is retrieved from the URL kwargs (request query).
        If the region is not found in the list of valid regions, a 404 error is raised
        """
        urls    = URLs()
        region  = self.kwargs.get("region")
        ratings = Rating.objects.filter(
            region = region
        )

        if region.upper() not in urls.regions:
            raise Http404(
                f"No ratings found. Region: {region} - (GL, RU, DE, US, FR, CN, PL, KR, JP, EN)"
            )

        return ratings

    def get_serializer_context(self) -> dict:
        """
        The context includes the request object and a boolean indicating
        whether the ratings should be displayed in days or hours
        """
        context = super().get_serializer_context()
        context.update(
            {
                "in_days": self.request.GET.get("in_days", "false"),
            }
        )

        return context