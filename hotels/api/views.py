from rest_framework.generics import ListAPIView
from hotels.models import Hotel
from .serializers import HotelListSerializer


class HotelList(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
