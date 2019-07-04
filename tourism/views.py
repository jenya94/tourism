from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate


def home_page(request):
    return render(request, 'common/home.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def login_user(request):
    user = authenticate(username='jenis5', password='jenisbay1994')
    if user is not None:
        login(request, user)
    return redirect('/')
