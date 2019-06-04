from rest_framework.serializers import ModelSerializer
from sightseeing.models import Sightseeing


class SightseeingListSerializer(ModelSerializer):
    class Meta:
        model = Sightseeing
        fields = '__all__'
