from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Discount, ItemInOrder, Order, Tax


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
                    'В заказе должен быть один товар'
                )


class ItemInOrderInline(admin.StackedInline):
    model = ItemInOrder
    extra = 0
    formset = ItemInOrderFormSet
    fields = ('item', 'amount')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    model = Discount
    fields = ('name', 'percentage', 'order')
    list_display = ('name', 'percentage', 'order')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
    inlines = (ItemInOrderInline,)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    model = Tax
    list_display = ('name', 'percentage')
