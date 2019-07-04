from django.shortcuts import render, render_to_response, redirect
from .models import Hotel, RegistrationBook, Room, RegistrationBook, Booking
from django.contrib import messages


__all__ = [
    'list_hotels', 'detail_hotel', 'make_unregistration', 'view_rooms', 'make_registration'
]


def list_hotels(request):
    context = {
        'hotels': Hotel.objects.all()
    }
    return render(request, 'hotels/hotel_list.html', context)


def detail_hotel(request, hotel_id):
    context = {
        'hotel': Hotel.objects.get(id=hotel_id)
    }
    return render(request, 'hotels/hotel_detail.html', context)


def make_registration(request):
    if request.POST:
        registration_book = RegistrationBook.objects.get(hotel=request.POST.get('hotel_id'))
        booking = Booking(
            registration_book=registration_book, orderer=request.POST.get('name'),
            date_ordered=request.POST.get('ordered_date'), date_expired=request.POST.get('expired_date')
        )
        booking.save()
        messages.success(request, "You have just booked room.")
    return redirect(f"/hotels/{request.POST.get('hotel_id')}/")


def view_rooms(request, hotel_id):
    context = {
        'registrationbook': RegistrationBook.objects.get(hotel=hotel_id),
        'rooms': Room.objects.filter(hotel=hotel_id),
        'hotel': Hotel.objects.get(id=hotel_id)
    }
    return render(request, 'hotels/room.html', context)


def make_unregistration(request):
    pass
