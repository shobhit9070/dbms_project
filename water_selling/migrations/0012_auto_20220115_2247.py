# Generated by Django 2.0.7 on 2022-01-15 17:17

from django.db import migrations, models
import water_selling.models


class Migration(migrations.Migration):

    dependencies = [
        ('water_selling', '0011_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateTimeField(default=water_selling.models.one_day_hence),
        ),
    ]