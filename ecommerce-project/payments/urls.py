from django.urls import path
from .views import CreatePaymentIntentView, ConfirmPaymentView, stripe_webhook

urlpatterns = [
    path('create-payment-intent/', CreatePaymentIntentView.as_view(), name='create-payment-intent'),
    path('confirm-payment/', ConfirmPaymentView.as_view(), name='confirm-payment'),
    path('webhook/', stripe_webhook, name='stripe-webhook'),
]