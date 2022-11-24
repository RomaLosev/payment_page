from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Discount, Item, StripePrice, ItemInOrder, Order, Tax


class PriceInlineAdmin(admin.TabularInline):
    model = StripePrice
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


class ItemInOrderFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                pass
            if count < 1:
                raise ValidationError(
                    'В заказе должен быть хоть один товар'
                )


class ItemInOrderInline(admin.StackedInline):
    model = ItemInOrder
    extra = 1
    formset = ItemInOrderFormSet
    fields = ('item', 'amount')


class DiscountAdmin(admin.ModelAdmin):
    model = Discount
    fields = ('name', 'percentage', 'order')
    list_display = ('name', 'percentage', 'order')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
    inlines = (ItemInOrderInline,)


class TaxAdmin(admin.ModelAdmin):
    model = Tax
    list_display = ('name', 'percentage')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax, TaxAdmin)

# from django.contrib import admin
#
# from .models import Item, StripePrice
#
#
# class PriceInlineAdmin(admin.TabularInline):
#     model = StripePrice
#     extra = 0
#
#
# class ItemAdmin(admin.ModelAdmin):
#     inlines = [PriceInlineAdmin]
#
#
# admin.site.register(Item, ItemAdmin)
