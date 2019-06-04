from rest_framework.serializers import ModelSerializer
from hotels.models import Hotel


class HotelListSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

