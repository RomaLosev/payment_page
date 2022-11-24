from django.urls import path

from items.views import (
    CreateCheckoutSessionView,
    ItemPage,
    ItemsMainPage,

)

app_name = 'items'

urlpatterns = [
    path(
        'buy/<pk>/', CreateCheckoutSessionView.as_view(),
        name='create-checkout-session'
    ),
    path('item/<pk>/', ItemPage.as_view(), name='item_page'),
]
