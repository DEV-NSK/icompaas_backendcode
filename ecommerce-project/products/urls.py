from django.urls import path
from .views import (ProductList, ProductDetail, CategoryList, 
                   ReviewCreate, ReviewList, ReviewUpdateDelete, ProductImageCreateView,
                   ProductCreateView, ProductUpdateDeleteView )

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/<int:product_id>/reviews/', ReviewList.as_view(), name='product-reviews'),
    path('products/<int:product_id>/reviews/create/', ReviewCreate.as_view(), name='review-create'),
    path('products/<int:product_id>/images/', ProductImageCreateView.as_view(), name='product-images'),
    path('reviews/<int:pk>/', ReviewUpdateDelete.as_view(), name='review-detail'),
    path('admin/products/', ProductCreateView.as_view(), name='product-create'),
    path('admin/products/<int:pk>/', ProductUpdateDeleteView.as_view(), name='product-admin-detail'),
]