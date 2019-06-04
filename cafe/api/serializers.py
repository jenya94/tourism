from rest_framework.serializers import ModelSerializer
from cafe.models import Eatery


class EateryListSerializer(ModelSerializer):
    class Meta:
        model = Eatery
        fields = '__all__'
