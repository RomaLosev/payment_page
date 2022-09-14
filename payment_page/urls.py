from django.contrib import admin
from django.urls import path
from items.views import (
    CreateCheckoutSessionView,
    ItemsMainPage,
    ItemPage,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('item/<pk>/', ItemPage.as_view(), name='item_page'),
    path('', ItemsMainPage.as_view(), name='main'),
]
