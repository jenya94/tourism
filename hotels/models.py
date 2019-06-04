from django.db import models
from django.contrib.auth.models import User
from money.models import Currency


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    photo = models.ImageField()
    price = models.PositiveIntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default=0)


class Room(models.Model):
    name = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField()


class Registration(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    date_ordered = models.DateField()
    date_expired = models.DateField()
    customer = models.CharField(max_length=100)
    room = models.PositiveIntegerField()
