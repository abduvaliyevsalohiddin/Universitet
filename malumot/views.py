from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def homepage(request):
    return render(request, "home.html")


def hamma_yonalishlar(request):
    if request.method == 'POST':
        Yonalish.objects.create(
            nom=request.POST.get("nom"),
            aktiv=request.POST.get("aktiv") == "on",
        )
    content = {
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, "hamma_yonalishlar.html", content)


def yonalish_ochir(request, son):
    Yonalish.objects.get(id=son).delete()
    return redirect("/hamma_yonalishlar/")


def hamma_fanlar(request):
    if request.method == 'POST':
        Fan.objects.create(
            nom=request.POST.get("nom"),
            yonalish=Yonalish.objects.get(id=request.POST.get("yonalish")),
            asosiy=request.POST.get("asosiy") == "on",
        )
    soz = request.GET.get("qidirish_sozi")
    natija = Fan.objects.all()
    if soz:
        natija = natija.filter(nom__contains=soz)
    content = {
        "fanlar": natija,
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, "hamma_fanlar.html", content)


def fan_ochir(request, son):
    Fan.objects.get(id=son).delete()
    return redirect("/hamma_fanlar/")


def hamma_ustozlar(request):
    if request.method == 'POST':
        Ustoz.objects.create(
            ism=request.POST.get("ism"),
            jins=request.POST.get("jins"),
            yosh=request.POST.get("yosh"),
            daraja=request.POST.get("daraja"),
            fan=Fan.objects.get(id=request.POST.get("fan")),
        )
    soz = request.GET.get("qidirish_sozi")
    natija = Ustoz.objects.all()
    if soz:
        natija = natija.filter(ism__contains=soz)
    content = {
        "ustozlar": natija,
        "fanlar": Fan.objects.all()
    }
    return render(request, "hamma_ustozlar.html", content)
