from django.urls import path
from .views import *


urlpatterns = [
    path('sightseeing/list', SightseeingListAPIView.as_view()),
]
