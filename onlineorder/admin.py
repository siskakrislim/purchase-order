from django.contrib import admin
from .models import Order, Product
# Register your models here.

admin.site.register(Order)
admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','status','purchaser','order_date','order_id')
    list_filter = ('status','order_date')

    fieldsets = (
        (None, {
            'fields': ('product','order_id')
        }),
        ('Availability', {
            'fields': ('status','order_date','purchaser')
        })
    )
