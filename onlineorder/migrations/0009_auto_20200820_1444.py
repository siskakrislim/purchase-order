# Generated by Django 2.2.15 on 2020-08-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineorder', '0008_auto_20200820_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
    ]
