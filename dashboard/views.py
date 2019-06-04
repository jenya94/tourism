# Django methods, libraries, apps
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
# Our apps, methods
from hotels.models import Hotel
from hotels.forms import AddHotelForm, EditHotelForm
from cafe.forms import AddEateryForm
from sightseeing.forms import AddSightseeingForm
from cafe.models import Eatery, Food, Menu
from sightseeing.models import Sightseeing


@login_required(login_url='/dashboard/login/')
def home_page(request):
    return render(request, 'dashboard/dashboard.html', {'title': 'Dashboard'})


def login_dashboard_user(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                next_page = request.GET['next']
            except MultiValueDictKeyError:
                next_page = '/dashboard/'
            return redirect(next_page)
    return render(request, 'dashboard/login.html')


@login_required(login_url='/dashboard/login/')
def logout_dashboard_user(request):
    logout(request)
    return redirect('/dashboard/login/')


def signup_dashboard_user(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, "Password and Confirm password is not valid.")
            return render(request, 'dashboard/signup.html', {'username': username, 'email': email})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.warning(request, "This username already exists.")
            return render(request, 'dashboard/signup.html', {'username': username, 'email': email})
        else:
            User.objects.create_user(username, email, password)
            return redirect('/dashboard/login/')
    return render(request, 'dashboard/signup.html')


@login_required(login_url='/dashboard/login/')
def user_profile(request):
    return render(request, 'dashboard/profile.html')


# Function to give service of hotels
# add, remove, list, change, detail

@login_required(login_url='/dashboard/login/')
def introduce_about_hotels(request):
    return render(request, 'dashboard/hotel/introduction_about_hotels.html')


@login_required(login_url='/dashboard/login/')
def list_hotel(request):
    context = {
        'hotels': Hotel.objects.filter(owner=request.user.id)
    }
    return render(request, 'dashboard/hotel/hotel_list.html', context)


@login_required(login_url='/dashboard/login/')
def add_hotel(request):
    if request.POST:
        form = AddHotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/hotel/add')
    context = {
        'form': AddHotelForm()
    }
    return render(request, 'dashboard/hotel/add_hotel.html', context)


@login_required(login_url='/dashboard/login/')
def remove_hotel(request, hotel_id):
    return render(request, 'dashboard/hotel/remove_hotel.html')


@login_required(login_url='/dashboard/login/')
def change_hotel_details(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    if request.POST:
        form = EditHotelForm(request.POST)
        if form.is_valid():
            hotel.name = request.POST['name']
            hotel.address = request.POST['address']
            hotel.phone_number = request.POST['phone_number']
            hotel.email = request.POST['email']
            hotel.owner = request.user
            hotel.save()
            return redirect('/dashboard/hotel/add')
    else:
        context = {
            'form': EditHotelForm(initial={
                'name': hotel.name,
                'address': hotel.address,
                'phone_number': hotel.phone_number,
                'email': hotel.email
            }),
            'hotel': hotel
        }
        return render(request, 'dashboard/hotel/change_hotel_details.html', context)
    return redirect('/dashboard/')


@login_required(login_url='/dashboard/login/')
def detail_hotel(request, hotel_id):
    context = {
        'hotel': Hotel.objects.get(id=hotel_id)
    }
    return render(request, 'dashboard/hotel/detail_hotel.html', context)


# Function to give service of hotels
# add, remove, list, change, detail


@login_required(login_url='/dashboard/login/')
def introduce_about_eateries(request):
    return render(request, 'dashboard/eatery/introduction_about_eateries.html')


@login_required(login_url='/dashboard/login/')
def list_eatery(request):
    context = {
        'eateries': Eatery.objects.filter(owner=request.user.id)
    }
    return render(request, 'dashboard/eatery/eatery_list.html', context)


@login_required(login_url='/dashboard/login/')
def add_eatery(request):
    if request.POST:
        form = AddEateryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/eatery/add/')
    context = {
        'form': AddEateryForm()
    }
    return render(request, 'dashboard/eatery/add_eatery.html', context)


@login_required(login_url='/dashboard/login/')
def remove_eatery(request, eatery_id):
    return render(request, 'dashboard/eatery/remove_hotel.html')


@login_required(login_url='/dashboard/login/')
def change_eatery_details(request, eatery_id):
    return render(request, 'dashboard/eatery/change_eatery_details.html')


@login_required(login_url='/dashboard/login/')
def detail_eatery(request, eatery_id):
    return render(request, 'dashboard/eatery/detail_hotel.html')


# Function to give service of hotels
# add, remove, list, change, detail


@login_required(login_url='/dashboard/login/')
def introduce_about_sightseeing(request):
    return render(request, 'dashboard/sightseeing/introduction_about_sightseeings.html')


@login_required(login_url='/dashboard/login/')
def list_sightseeing(request):
    context = {
        'sightseeings': Sightseeing.objects.filter(owner=request.user.id)
    }
    return render(request, 'dashboard/sightseeing/sightseeing_list.html', context)


@login_required(login_url='/dashboard/login/')
def add_sightseeing(request):
    if request.POST:
        form = AddSightseeingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/sightseeing/add/')
    context = {
        'form': AddSightseeingForm()
    }
    return render(request, 'dashboard/sightseeing/add_sightseeing.html', context)


@login_required(login_url='/dashboard/login/')
def remove_sightseeing(request, sightseeing_id):
    return render(request, 'dashboard/sightseeing/remove_sightseeing.html')


@login_required(login_url='/dashboard/login/')
def change_sightseeing_details(request, sightseeing_id):
    return render(request, 'dashboard/sightseeing/change_sightseeing_details.html')


@login_required(login_url='/dashboard/login/')
def detail_sightseeing(request, sightseeing_id):
    return render(request, 'dashboard/sightseeing/detail_hotel.html')
