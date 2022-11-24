from django.contrib import admin

from .models import Item, StripePrice


class PriceInlineAdmin(admin.TabularInline):
    model = StripePrice
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]
