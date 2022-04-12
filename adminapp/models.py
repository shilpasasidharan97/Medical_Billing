
from email.policy import default
from django.db import models

# Create your models here.

class Medicines(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    purchase_cost=models.FloatField()
    selling_cost=models.FloatField()
    description=models.CharField(max_length=500)
    quantity=models.IntegerField()

    class Meta:
        db_table='medicine'


class SaledMedicine(models.Model):
    id=models.AutoField(primary_key=True)
    medicines=models.ForeignKey(Medicines,on_delete=models.CASCADE)
    Bill_number=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=50)
    customer_phonenum=models.CharField(max_length=15)
    # date=models.DateField(default=0)
    quantity=models.IntegerField()
    item_price=models.FloatField()
    gst=models.FloatField()
    grand_total=models.FloatField()

    class Meta:
        db_table='sellings'


