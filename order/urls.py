from django.urls import path

from order.views import CreateCheckoutSessionOrderView, OrderView

app_name = 'order'

urlpatterns = [
    path(
        'order/<pk>/',
        OrderView.as_view(),
        name='order_page',
    ),
    path(
        'pay_for_order/<pk>/',
        CreateCheckoutSessionOrderView.as_view(),
        name='order_pay',
    ),
]
