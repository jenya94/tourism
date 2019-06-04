from django.urls import path, include
from .views import *


urlpatterns = [
    path('list/', list_sightseeing),
    path('detail/<int:sightseeing_id>/', detail_sightseeing),
    path('api/', include('sightseeing.api.urls')),
]
