from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

profielen = [
    {"naam": "Jan de Eerste", "geboortedatum": "28-12-2018"},
    {"naam": "Piet de Tweede", "geboortedatum": "28-11-2013"},
]


def profiel_lijst(request):
    context = {"profielen": profielen}
    return render(request, "profiel/profielen_lijst.html", context)


def profiel_detail(request, profiel):
    context = {"profiel": profiel}
    return render(request, "profiel/profielen_detail.html", context)


def profiel_create(request, profiel=None):
    return HttpResponse("<h1>Profiel create</h1>")

