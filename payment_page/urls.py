from django.contrib import admin
from django.urls import include, path

from items.views import ItemsMainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ItemsMainPage.as_view(), name='main'),
    path('', include('items.urls', namespace='items')),
    path('', include('order.urls', namespace='order')),
]
