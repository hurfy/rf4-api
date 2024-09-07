from rest_framework          import generics
from django.http             import Http404

from apps.api.serializers    import RecordSerializer
from apps.parser.services    import REGIONS, CATEGORIES
from apps.api.paginators     import DefaultAPIPaginator
from apps.core.models        import Record


class RecordsAPIView(generics.ListAPIView):
    serializer_class = RecordSerializer
    pagination_class = DefaultAPIPaginator

    def get_queryset(self) -> Record:
        """
        The region and rec_type parameters are retrieved from the URL kwargs.
        If the region is not found in the list of valid regions, or rec_type is not found in the list of valid
        categories, a 404 error is raised
        """
        region   = self.kwargs.get("region")
        rec_type = self.kwargs.get("type")
        records  = Record.objects.filter(
            region   = region,
            rec_type = rec_type
        )

        if region.upper() not in REGIONS or rec_type not in CATEGORIES:
            raise Http404(
                f"No ratings found. Region: {region} - (GL, RU, DE, US, FR, CN, PL, KR, JP, EN) "
                f"Record type: {rec_type} - (records, ultralight, telestick)"
            )

        return records

    def get_serializer_context(self) -> dict:
        """
        The context includes the request object and a boolean indicating
        whether the records should be displayed in grams or pounds
        """
        context = super().get_serializer_context()
        context.update(
            {
                "in_gram": self.request.GET.get("in_gram", "false"),
            }
        )

        return context