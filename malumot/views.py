from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def homepage(request):
    return render(request, "home.html")


def hamma_yonalishlar(request):
    content = {
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, "hamma_yonalishlar.html", content)


def yonalish_ochir(request, son):
    Yonalish.objects.get(id=son).delete()
    return redirect("/hamma_yonalishlar/")


def hamma_fanlar(request):
    soz = request.GET.get("qidirish_sozi")
    natija = Fan.objects.all()
    if soz:
        natija = natija.filter(nom__contains=soz)
    content = {
        "fanlar": natija
    }
    return render(request, "hamma_fanlar.html", content)


def fan_ochir(request, son):
    Fan.objects.get(id=son).delete()
    return redirect("/hamma_fanlar/")


def hamma_ustozlar(request):
    soz = request.GET.get("qidirish_sozi")
    natija = Ustoz.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)
    content = {
        "ustozlar": natija
    }
    return render(request, "hamma_ustozlar.html", content)
