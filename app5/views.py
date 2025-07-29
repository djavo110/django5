from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CarForm

def avtosalon(request):
    salon = Avtosalon.objects.first()
    # brend = Brend.objects.all()
    car = Car.objects.filter(salon=salon)
    context = {
        "salon": salon,
        "car" : car
    }
    return render(request, 'index.html', context)

def brend(request, pk):
    avto = Avtosalon.objects.all()
    brend = Brend.objects.all()
    car = Car.objects.filter(brend=pk)
    context = {
        "title": "NEWS TITLE",
        "avto": avto,
        "brend" : brend,
        "car" : car
    }
    return render(request, 'brend.html', context=context)

def car(request, pk):
    # avto = Avtosalon.objects.all()
    # brend = Brend.objects.filter(car=pk)
    car = Car.objects.get(pk=pk)
    # context = {
    #     "title": "NEWS TITLE",
    #     "avto": avto,
    #     "brend" : brend,
    #     "car" : car
    # }
    return render(request, 'car.html', {"car": car})

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, "add_car.html", {"form": form})