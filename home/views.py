from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("ควย-")

def home(request):
    return HttpResponse("บ้านนนนนนนนน")