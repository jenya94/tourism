from django.shortcuts import render
from .models import Eatery, EateryType, Menu, Food


def list_eatery(request):
    context = {}
    query = Eatery.objects
    if request.POST:
        if 'name' in request.POST and request.POST.get('name') != '':
            query = query.filter(name=request.POST.get('name'))
        if 'eatery_type' in request.POST and request.POST.get('eatery_type') != '':
            query = query.filter(eatery_type=EateryType.objects.get(id=request.POST.get('eatery_type')))

    context['eatery_types'] = EateryType.objects.all()
    context['eateries'] = query.all()
    return render(request, 'cafe/eatery_list.html', context)


def detail_eatery(request, eatery_id):
    context = {
        'eatery': Eatery.objects.get(id=eatery_id)
    }
    return render(request, 'cafe/detail.html', context)


def view_menu(request, eatery_id):
    menu = Menu.objects.filter(eatery=eatery_id)
    list_menu_id = [m.id for m in menu]
    context = {
        'menu': menu,
        'foods': Food.objects.filter(menu__in=list_menu_id)
    }
    return render(request, 'cafe/menu.html', context)
