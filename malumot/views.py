from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def homepage(request):
    return render(request, "home.html")


def hamma_yonalishlar(request):
    content = {
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, "hamma_yonalishlar.html", content)


def hamma_fanlar(request):
    content = {
        "fanlar": Fan.objects.all()
    }
    return render(request, "hamma_fanlar.html", content)


def hamma_ustozlar(request):
    content = {
        "ustozlar": Ustoz.objects.all()
    }
    return render(request, "hamma_ustozlar.html", content)
