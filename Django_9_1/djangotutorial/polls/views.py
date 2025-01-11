from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")
def test(request):
    return HttpResponse("<h1>man test hastam.</h1>")