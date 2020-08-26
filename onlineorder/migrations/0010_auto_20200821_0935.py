# Generated by Django 3.0 on 2020-08-21 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineorder', '0009_auto_20200820_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uom',
            field=models.CharField(choices=[('1', 'PCS'), ('2', 'BAG'), ('3', 'ROLL/BOX'), ('4', 'BOX'), ('5', 'PAIL'), ('6', 'BOTTLE'), ('7', 'UNIT'), ('8', 'CAN'), ('9', 'SET')], default='', max_length=1, verbose_name='UOM (Unit of Measurement)'),
        ),
    ]