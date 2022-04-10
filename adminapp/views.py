from django.shortcuts import render

from adminapp.models import Medicines

# Create your views here.


def home(request):
    return render(request,'admin_home.html')


def add_medicine(request):

    msg=""
    if request.method=='POST':
        med_name=request.POST['name']
        purchase_cost=request.POST['pcost']
        selling_cost=request.POST['scost']
        quantity=request.POST['quantity']
        description=request.POST['description']

        new_medicine=Medicines(name=med_name,purchase_cost=purchase_cost,selling_cost=selling_cost,description=description,quantity=quantity)
        new_medicine.save()

        msg="The medicine is added to the list"
    else:
        msg="The medicine is already exists in the list"

    return render(request,'add_medicine.html',{'message':msg,})

def add_pharmacist(request):
    return render(request,'add_pharmacist.html')

def view_medicine(request):
    medicines=Medicines.objects.all()
    return render(request,'view_med.html',{'med':medicines,})

def purchase_list(request):
    med=Medicines.objects.filter(quantity__lte=10)
    return render(request,'purchase_list.html',{'med':med,})

def billing(request):
    return render(request,'billing.html')