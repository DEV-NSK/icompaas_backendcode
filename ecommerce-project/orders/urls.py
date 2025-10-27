from django.urls import path
from .views import (CartDetailView, AddToCartView, UpdateCartItemView, 
                   RemoveFromCartView, OrderListCreateView, OrderDetailView)

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/items/<int:item_id>/update/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('cart/items/<int:item_id>/remove/', RemoveFromCartView.as_view(), name='remove-cart-item'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]