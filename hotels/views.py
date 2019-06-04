from django.shortcuts import render, render_to_response, redirect
from .models import Hotel, Registration, Room
from django.contrib import messages


__all__ = [
    'list_hotels', 'detail_hotel', 'make_registration', 'make_unregistration', 'view_rooms'
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


def view_rooms(request, hotel_id):
    context = {
        'rooms': Room.objects.filter(hotel=hotel_id),
        'hotel': Hotel.objects.get(id=hotel_id)
    }
    return render(request, 'hotels/room.html', context)


def make_registration(request):
    if request.POST:
        registration = Registration(
            customer=request.POST.get('customer'),
            date_ordered=request.POST.get('date_ordered'),
            date_expired=request.POST.get('date_expired'),
            room=request.POST.get('room'),
            hotel=Hotel.objects.get(id=request.POST.get('hotel_id'))
        )
        registration.save()
        messages.success(request, 'You just booked the room.')
        return redirect(f"/hotel/detail/{request.POST.get('hotel_id')}/")

    return redirect('/hotel/list/')


def make_unregistration(request):
    pass
