from django.urls import path
from . import views as my_views

urlpatterns = [
    path('', my_views.products, name='products-url'),
    path('add-products/', my_views.add_products, name='add-products-url'),
    path('update-products/', my_views.update_products, name='view-products-url'),
    path('shop/', my_views.shop, name='shop-url'),
]
