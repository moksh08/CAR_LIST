from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_app/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    return render(request, 'car_app/car_detail.html', {'car': car})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_app/car_form.html', {'form': form})

def car_update(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_app/car_form.html', {'form': form, 'car': car})

def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    car.delete()
    return redirect('car_list')
