# """
# URL configuration for ecommerce_backend project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]











# # ecommerce_backend/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def api_root(request):
#     return Response({
#         'message': 'Ecommerce API is running successfully! 🚀',
#         'endpoints': {
#             'admin': '/admin/',
#             'auth_register': '/api/auth/register/',
#             'auth_login': '/api/auth/login/',
#             'products': '/api/products/',
#             'categories': '/api/categories/',
#             'orders': '/api/orders/',
#             'cart': '/api/cart/',
#             'payments': '/api/payments/'
#         },
#         'status': 'active'
#     })

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/auth/', include('users.urls')),
#     path('api/', include('products.urls')),
#     path('api/', include('orders.urls')),
#     path('api/payments/', include('payments.urls')),
#     path('api/', api_root, name='api-root'),  # Add this line for /api/
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # ecommerce_backend/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET'])
# def api_root(request):
#     return Response({
#         'message': 'Ecommerce API is running successfully! 🚀',
#         'endpoints': {
#             'admin': '/admin/',
#             'auth_register': '/api/auth/register/',
#             'auth_login': '/api/auth/login/',
#             'products': '/api/products/',
#             'categories': '/api/categories/',
#             'orders': '/api/orders/',
#             'cart': '/api/cart/',
#             'payments': '/api/payments/'
#         },
#         'status': 'active'
#     })

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/auth/', include('users.urls')),
#     path('api/', include('products.urls')),
#     path('api/', include('orders.urls')),
#     path('api/payments/', include('payments.urls')),
#     path('api/', api_root, name='api-root'),  # Add this line for /api/
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ecommerce_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    """
    API Root endpoint showing available endpoints
    """
    return Response({
        'message': 'Ecommerce API is running successfully! 🚀',
        'version': '1.0',
        'status': 'active',
        'endpoints': {
            'admin': '/admin/',
            'authentication': {
                'register': '/api/auth/register/',
                'login': '/api/auth/login/',
                'profile': '/api/auth/profile/'
            },
            'products': {
                'list': '/api/products/',
                'categories': '/api/categories/',
                'featured': '/api/products/?featured=true'
            },
            'orders': '/api/orders/',
            'payments': '/api/payments/',
            'cart': '/api/cart/'
        },
        'documentation': 'Add /admin/ for Django admin interface'
    })

urlpatterns = [
    # Root API endpoint
    path('', api_root, name='api-root'),
    
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Authentication endpoints
    path('api/auth/', include('users.urls')),
    
    # Products and categories endpoints
    path('api/', include('products.urls')),
    
    # Orders endpoints
    path('api/', include('orders.urls')),
    
    # Payments endpoints
    path('api/payments/', include('payments.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Also serve static files in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)