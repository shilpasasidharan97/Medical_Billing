from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'admin_home.html')


def add_medicine(request):
    return render(request,'add_medicine.html')

def add_pharmacist(request):
    return render(request,'add_pharmacist.html')

def view_medicine(request):
    return render(request,'view_med.html')