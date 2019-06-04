from django.urls import path, include
from .views import *


urlpatterns = [
    path('list/', list_hotels),
    path('detail/<int:hotel_id>/', detail_hotel),
    path('registration/', make_registration),
    path('<int:hotel_id>/rooms/', view_rooms),
    path('api/', include('hotels.api.urls')),
]
