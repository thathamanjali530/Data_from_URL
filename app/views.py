from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def data_from_url(request,Name):
    return HttpResponse(f'Hai {Name} How Are You')
