# Generated by Django 2.2.15 on 2020-08-20 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineorder', '0004_auto_20200820_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='order',
            name='product_code',
            field=models.CharField(verbose_name='JOE PANEL PRODUCT CODE',default='',max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
