from random import Random, random
from django.shortcuts import render
import random

from adminapp.models import Medicines, SaledMedicine

# Create your views here.


def home(request):
    return render(request, 'admin_home.html')


def add_medicine(request):

    msg = ""
    if request.method == 'POST':
        med_name = request.POST['name']
        purchase_cost = request.POST['pcost']
        selling_cost = request.POST['scost']
        quantity = request.POST['quantity']
        description = request.POST['description']

        new_medicine = Medicines(name=med_name, purchase_cost=purchase_cost,
                                 selling_cost=selling_cost, description=description, quantity=quantity)
        new_medicine.save()

        msg = "The medicine is added to the list"

    return render(request, 'add_medicine.html', {'message': msg, })


def add_pharmacist(request):
    return render(request, 'add_pharmacist.html')


def view_medicine(request):
    medicines = Medicines.objects.all()
    return render(request, 'view_med.html', {'med': medicines, })


def purchase_list(request):
    med = Medicines.objects.filter(quantity__lte=10)
    return render(request, 'purchase_list.html', {'med': med, })


def billing(request):
    # if 'name' in request.GET:
    #     name=request.GET['name']
    #     medicines=Medicines.objects.filter(name__icontaines=name)
    # else:
    #     medicines=Medicines.objects.all()

    billnumber = ""
    gst=""  
    item_price=""

    rand = random.randint(10000, 99999)
    billnumber = 'abc'+str(rand)

    if request.method == 'POST':
        billnumber=billnumber
        customer_name=request.POST['cname']
        customer_phonenumber=request.POST['phn']
        # date=request.POST['date']
        mname = request.POST['mname']
        quantity = request.POST['quantity']
        item_price=request.POST['itemprice']
        gst=request.POST['gst']
        grand_total=request.POST['grandtotal']
        medicine_quantity = Medicines.objects.get(id=mname)

        saled_medicine=SaledMedicine(medicines_id=mname,Bill_number=billnumber,customer_name=customer_name,customer_phonenum=customer_phonenumber,quantity=quantity,item_price=item_price,gst=gst,grand_total=grand_total)

        saled_medicine.save()

        medicine_quantity.quantity = medicine_quantity.quantity - int(quantity)
        medicine_quantity.save()

    medicines = Medicines.objects.all()

    return render(request, 'billing.html', { 'med': medicines,'billnum':billnumber })


def price_show(request):
    id = request.GET['id']
    # print(id)
    try:
        price = Medicines.objects.get(id=id)
        print(price)
        return render(request, 'price.html', {'price': price.selling_cost})
    except:
        return render(request, 'price.html', {'price': 0})


def total_price(request):
    price = request.GET['uprice']
    qty = request.GET['qty']
    try:
        total_price = int(qty) * int(price)
        print(total_price)
        gst = (total_price * 5)/100
        grand_total = int(total_price)+int(gst)
        # print(total_price)
        # print(gst)
        # print(grand_total)
        return render(request, 'total.html', {'total_price': total_price})
    except:
        return render(request, 'total.html', {'total_price': 0})


def gst(request):

    med = request.GET['id']
    qty = request.GET['qty']

    medicine = Medicines.objects.get(id=med)
    selling_cost = medicine.selling_cost
    total = int(selling_cost) * int(qty)
    gst = (total * 5)/100
    # print(gst)

    return render(request, 'gst.html', {'gst': gst, })


def grand_total(request):

    med = request.GET['id']
    qty = request.GET['qty']

    medicine = Medicines.objects.get(id=med)
    selling_cost = medicine.selling_cost
    total = int(selling_cost) * int(qty)
    gst = (total * 5)/100
    grand_total = total + gst
    print(grand_total)

    return render(request, 'grand_total.html', {'grand_total': grand_total, })
