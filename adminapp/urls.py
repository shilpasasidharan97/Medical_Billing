from django import views
from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('addmedicine',views.add_medicine,name='addmedicine'),
    path('addpharmacist',views.add_pharmacist,name='addpharmacist'),
    path('viewmedicine',views.view_medicine,name='viewmed'),
    path('purchaselist',views.purchase_list,name='purchaselist'),
    path('billing',views.billing,name='billing'),
    path('price',views.price_show, name='price'),
    path('total',views.total_price, name='total'),
     path('gst',views.gst, name='gst'),
    path('grandtotal',views.grand_total, name='grandtotal'),
    
]
