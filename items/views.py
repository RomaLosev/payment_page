import stripe
from django import views
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView

from items.models import Item, StripePrice, Order, ItemInOrder

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemsMainPage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        items = Item.objects.all()
        context = {
            'items': items,
        }
        return context


class ItemPage(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        item = get_object_or_404(Item, id=item_id)
        price = StripePrice.objects.filter(item=item)
        context = {
            'item': item,
            'price': price,
            'currency': item.currency,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        }
        return context


class OrderView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        order_id = self.kwargs['pk']
        order = get_object_or_404(Order, id=order_id)
        items = ItemInOrder.objects.filter(order_id=order_id)
        amount = sum(item.amount * float(item.item.price) for item in items) / 100
        context = {
            'order': order,
            'items': items,
            'amount': amount,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        }
        return context


class CreateCheckoutSessionView(views.View):

    def get(self, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return JsonResponse({
            'id': session.id
        })


class CreateCheckoutSessionOrderView(views.View):

    def get(self, *args, **kwargs):
        order_id = self.kwargs['pk']
        order = get_object_or_404(Order, id=order_id)
        items = ItemInOrder.objects.filter(order_id=order_id)
        discount = None
        if order.discount.count() > 0:
            discount = order.discount.all()[0]
            coupon = stripe.Coupon.create(
                name=discount.name,
                percent_off=discount.percentage,
                duration='once',
            )
            discount = [
                {
                    'coupon': coupon
                }
            ]
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'unit_amount': item.item.price,
                        'currency': item.item.currency,
                        'product_data': {
                            'name': item.item.name
                        }
                    },
                    'quantity': item.amount,
                }
                for item in items],
            discounts=discount,
            # payment_method_types=['card'],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return JsonResponse({
            'id': session.id
        })
