from django.urls import path
from .views import *

urlpatterns = [
    path('eatery/list', EateryListAPIView.as_view()),
]