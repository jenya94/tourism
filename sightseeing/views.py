from django.shortcuts import render
from .models import Sightseeing
__all__ = [
    'list_sightseeing', 'detail_sightseeing'
]


def list_sightseeing(request):
    context = {
        'sightseeings': Sightseeing.objects.all()
    }
    return render(request, 'sightseeing/list_sightseeing.html', context)


def detail_sightseeing(request, sightseeing_id):
    context = {
        'sightseeing': Sightseeing.objects.get(id=sightseeing_id)
    }
    return render(request, 'sightseeing/detail_sightseeing.html', context)
