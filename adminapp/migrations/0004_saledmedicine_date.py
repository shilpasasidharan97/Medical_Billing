# Generated by Django 3.2.9 on 2022-04-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_rename_medicines_saledmedicine_medicines'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledmedicine',
            name='date',
            field=models.DateField(default=0),
        ),
    ]
