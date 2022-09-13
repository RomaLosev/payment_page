from django.contrib import admin
from .models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'total_price',
    )
