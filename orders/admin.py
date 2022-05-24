from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['customer','size','order_status','quantity','created_date']

    list_filter=['created_date','order_status','size']

# Register your models here.
