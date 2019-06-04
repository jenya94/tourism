from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    # Home page of dashboard
    path('', home_page),
    # Login and logout pages of dashboard
    path('login/', login_dashboard_user),
    path('signup/', signup_dashboard_user),
    path('logout/', logout_dashboard_user),
    path('profile/', user_profile),
    # Hotels
    path('hotel/', introduce_about_hotels),
    path('hotel/add/', add_hotel),
    path('hotel/list/', list_hotel),
    path('hotel/detail/<int:hotel_id>/', add_hotel),
    path('hotel/remove/<int:hotel_id>/', remove_hotel),
    path('hotel/edit/<int:hotel_id>/', change_hotel_details),
    # Eateries
    path('eatery/', introduce_about_eateries),
    path('eatery/add/', add_eatery),
    path('eatery/list/', list_eatery),
    path('eatery/detail/<int:eatery_id>/', add_eatery),
    path('eatery/remove/<int:eatery_id>/', remove_eatery),
    path('eatery/change/<int:eatery_id>/', change_eatery_details),
    # Sightseeings
    path('sightseeing/', introduce_about_sightseeing),
    path('sightseeing/add/', add_sightseeing),
    path('sightseeing/list/', list_sightseeing),
    path('sightseeing/detail/<int:sightseeing_id>/', add_sightseeing),
    path('sightseeing/remove/<int:sightseeing_id>/', remove_sightseeing),
    path('sightseeing/change/<int:sightseeing_id>/', change_sightseeing_details),
]