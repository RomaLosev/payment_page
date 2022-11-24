import stripe
from django import views
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from items.models import Item, StripePrice

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
