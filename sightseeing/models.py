from django.db import models
from django.contrib.auth.models import User
from money.models import Currency


class Sightseeing(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(default=None)
    price = models.PositiveIntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default=0)
