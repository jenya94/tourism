from rest_framework.generics import ListAPIView
from sightseeing.models import Sightseeing
from .serializers import SightseeingListSerializer


class SightseeingListAPIView(ListAPIView):
    queryset = Sightseeing.objects.all()
    serializer_class = SightseeingListSerializer
