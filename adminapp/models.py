
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