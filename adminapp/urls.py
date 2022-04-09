from django import views
from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('home',views.home,name='home'),
    path('addmedicine',views.add_medicine,name='addmedicine'),
    path('addpharmacist',views.add_pharmacist,name='addpharmacist'),
    path('viewmedicine',views.view_medicine,name='viewmed')
]
