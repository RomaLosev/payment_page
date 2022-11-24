from django.contrib import admin
from django.urls import path

from items.views import (
    CreateCheckoutSessionView,
    CreateCheckoutSessionOrderView,
    ItemPage,
    OrderView,
    ItemsMainPage,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'buy/<pk>/', CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'
    ),
    path('item/<pk>/', ItemPage.as_view(), name='item_page'),
    path('order/<pk>/', OrderView.as_view(), name='order_page'),
    path('pay_for_order/<pk>/', CreateCheckoutSessionOrderView.as_view(), name='order_pay'),
    path('', ItemsMainPage.as_view(), name='main'),
]
