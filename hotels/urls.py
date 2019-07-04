from django.urls import path, include
from .views import *


urlpatterns = [
    path('', list_hotels, name="list"),
    path('booking/', make_registration, name='booking'),
    path('<int:hotel_id>/', view_rooms, name='hotel'),

]
