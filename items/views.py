import stripe
from django import views
from django.http import JsonResponse
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(views.View):

    def create_checkout_session(self, request, *args, **kwargs):
        session = stripe.checkout.Session.create(
          line_items=[{
            'price_data': {
              'currency': 'usd',
              'product_data': {
                'name': 'T-shirt',
              },
              'unit_amount': 2000,
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