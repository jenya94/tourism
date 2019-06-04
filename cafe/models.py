from django.db import models
from django.contrib.auth.models import User
from money.models import Currency


class EateryType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Eatery(models.Model):
    eatery_type = models.ForeignKey(EateryType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    photo = models.ImageField()


class Menu(models.Model):
    eatery = models.ForeignKey(Eatery, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)


class Food(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default=0)
    image = models.ImageField()
