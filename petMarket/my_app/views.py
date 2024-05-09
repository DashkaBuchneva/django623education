from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('страница появилась')


def page_2(request):
    return HttpResponse('страница 2')
