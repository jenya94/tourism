from django.db import models
from django.contrib.auth.models import User
from money.models import Currency
from decimal import Decimal

from payments import PurchasedItem
from payments.models import BasePayment


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    image = models.ImageField()
    price = models.PositiveIntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, default=0)
    services = models.TextField(default="{}")


class Room(models.Model):
    name = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms_images')
    image = models.ImageField()


class RegistrationBook(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='registration_book')
    occupied_rooms = models.PositiveIntegerField(default=0)
    available_rooms = models.PositiveIntegerField(default=0)

    def book(self):
        self.available_rooms -= 1
        self.occupied_rooms += 1
        self.save()

    def unbook(self):
        self.available_rooms += 1
        self.occupied_rooms -= 1
        self.save()


class Booking(models.Model):
    registration_book = models.ForeignKey(RegistrationBook, models.CASCADE, related_name='bookings')
    orderer = models.CharField(max_length=500)
    date_ordered = models.DateField()
    date_expired = models.DateField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.registration_book.book()
        super(Booking, self).save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        self.registration_book.unbook()
        super(Booking, self).delete(using, keep_parents)


class Payment(BasePayment):
    def get_failure_url(self):
        return 'http://example.com/failure/'

    def get_success_url(self):
        return 'http://example.com/success/'

    def get_purchased_items(self):
        # you'll probably want to retrieve these from an associated order
        yield PurchasedItem(name='The Hound of the Baskervilles', sku='BSKV', quantity=9, price=Decimal(10), currency='USD')
