from django.shortcuts import render
from django.urls import reverse_lazy
from dynamicnav.models import AbstractPainting, WildlifePainting
from forposters.models import ShowPosters
from frames.models import TableTop

from . import forms


def index(request):
    return render(request, 'splash.html')


def contact(request):
    return render(request, 'contactus.html')


def home(request):
    abs_painting = AbstractPainting.objects.all()
    wild_painting = WildlifePainting.objects.all()
    show_poster = ShowPosters.objects.all()
    tableframe = TableTop.objects.all()

    dict = {
        "abs_painting": abs_painting,
        "wild_painting": wild_painting,
        "show_poster": show_poster,
        "tableframe": tableframe,
    }
    return render(request, 'index.html', dict)


