from django.shortcuts import render, render_to_response, redirect
from .models import Hotel, RegistrationBook, Room, RegistrationBook, Booking
from django.contrib import messages
from payments import get_payment_model
from decimal import Decimal
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

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
        token = request.POST.get('stripeToken')
        charge = stripe.Charge.create(
            amount="100",
            currency="USD",
            description="Example Payment",
            source=token
        )

        messages.success(request, "You have just booked room.")
    return redirect(f"/hotels/{request.POST.get('hotel_id')}/")


def view_rooms(request, hotel_id):
    context = {
        'registrationbook': RegistrationBook.objects.get(hotel=hotel_id),
        'rooms': Room.objects.filter(hotel=hotel_id),
        'hotel': Hotel.objects.get(id=hotel_id),
        'pb_key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'hotels/room.html', context)


def make_unregistration(request):
    pass


def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))
    return TemplateResponse(request, 'payment.html', {'form': form, 'payment': payment})
