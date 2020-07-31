from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    dest = Destinations.objects.all()
    return render(request, 'index2.html',{'dest':dest})
