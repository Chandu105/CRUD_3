from django.shortcuts import render
from app.models import *
# Create your views here.
def display_country(request):
    QLCO=Country.objects.all()
    d={'QLCO':QLCO}
    return render(request,'display_country.html',d)
def display_capital(request):
    QLCPO=Capital.objects.all()
    d={'QLCPO':QLCPO}
    return render(request,'display_capital.html',d)