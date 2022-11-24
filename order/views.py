from decimal import Decimal

import stripe
from django import views
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from order.models import ItemInOrder, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        order_id = self.kwargs['pk']
        order = get_object_or_404(Order, id=order_id)
        items = ItemInOrder.objects.filter(order_id=order_id)
        amount = sum(
            item.amount * Decimal(item.item.price) for item in items
        ) / 100
        context = {
            'order': order,
            'items': items,
            'amount': amount,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        }
        return context


class CreateCheckoutSessionOrderView(views.View):

    @staticmethod
    def tax(order):
        if order.tax.count() != 0:
            tax = order.tax.all()[0]
            tax_rates = stripe.TaxRate.create(
                display_name='Tax',
                inclusive=tax.inclusive,
                percentage=tax.percentage,
            )
            return [tax_rates['id']]

    @staticmethod
    def coupon(order):
        if order.discount.count() != 0:
            discount = order.discount.all()[0]
            coupon = stripe.Coupon.create(
                name=discount.name,
                percent_off=discount.percentage,
                duration='once',
            )
            return [{'coupon': coupon}]

    def get(self, *args, **kwargs):
        order_id = self.kwargs['pk']
        order = get_object_or_404(Order, id=order_id)
        items = ItemInOrder.objects.filter(order_id=order_id)
        tax = self.tax(order)
        discount = self.coupon(order)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'unit_amount': item.item.price,
                        'currency': item.item.currency,
                        'product_data': {
                            'name': item.item.name
                        },
                    },
                    'quantity': item.amount,
                    'tax_rates': tax,
                }
                for item in items],
            mode='payment',
            payment_method_types=['card'],
            discounts=discount,
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return JsonResponse({
            'id': session.id
        })
