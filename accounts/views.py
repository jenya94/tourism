from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
import json


__all__ = ['user_login', 'user_logout', 'user_signup', 'user_profile']


def user_login(request):
    if request.POST:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'account/login.html')


def user_signup(request):
    if request.POST:
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            try:
                User.objects.create_user(
                    username=request.POST.get('username'),
                    password=request.POST.get('password'),
                    email=request.POST.get('email'),
                    first_name=request.POST.get('firstname'),
                    last_name=request.POST.get('lastname')
                )
            except:
                pass
            else:
                user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
                login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            messages.warning(request, f"There is an user like this {request.POST.get('username')} username")

    return render(request, 'account/signup.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required
def user_profile(request):
    context = dict()
    try:
        from django.core.serializers import serialize, get_serializer, get_deserializer
        user = User.objects.get(id=request.user.id)
        request.user.email = json.loads(user.email)
        try:
            context['user_social'] = user.socialaccount_set.get(user=user.id)
        except Exception as exp:
            pass
    except Exception as exp:
        raise exp
    return render(request, 'account/profile.html', context)
