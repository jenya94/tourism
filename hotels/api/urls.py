from django.urls import path
from .views import *


urlpatterns = [
    path('hotel/list', HotelList.as_view()),
]