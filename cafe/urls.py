from django.urls import path, include
from .views import *


urlpatterns = [
    path('list/', list_eatery),
    path('detail/<int:eatery_id>/', detail_eatery),
    path('<int:eatery_id>/menu/', view_menu),
    path('api/', include('cafe.api.urls')),
]
