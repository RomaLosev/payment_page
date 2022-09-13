from django.contrib import admin
from django.urls import path
from payment_page.items.views import (
    CreateCheckoutSessionView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_checkout_session/', CreateCheckoutSessionView.as_view(), name='create_checkout_session')
]
