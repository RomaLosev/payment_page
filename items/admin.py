from django.contrib import admin

from .models import Item, StripePrice


class PriceInlineAdmin(admin.TabularInline):
    model = StripePrice
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


admin.site.register(Item, ItemAdmin)
