from rest_framework.generics import ListAPIView
from cafe.models import Eatery
from .serializers import EateryListSerializer


class EateryListAPIView(ListAPIView):
    queryset = Eatery.objects.all()
    serializer_class = EateryListSerializer
