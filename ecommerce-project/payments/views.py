import stripe
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentIntentView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        order = get_object_or_404(Order, id=order_id, user=request.user)
        
        # Validate order status
        if order.status != 'pending':
            return Response(
                {'error': 'Order already processed'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Create PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_amount * 100),  # Convert to cents
                currency='usd',
                metadata={
                    'order_id': order.id,
                    'user_id': request.user.id
                },
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            
            return Response({
                'clientSecret': intent.client_secret,
                'order_id': order.id,
                'amount': order.total_amount
            })
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ConfirmPaymentView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        payment_intent_id = request.data.get('payment_intent_id')
        order_id = request.data.get('order_id')
        
        try:
            # Retrieve payment intent
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            
            if intent.status == 'succeeded':
                # Update order status
                order = Order.objects.get(id=order_id, user=request.user)
                order.status = 'processing'
                order.save()
                
                return Response({
                    'status': 'success',
                    'message': 'Payment confirmed',
                    'order_status': order.status
                })
            else:
                return Response({
                    'status': 'failed',
                    'message': 'Payment not completed'
                }, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Webhook handler (for Stripe webhooks)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)
    
    # Handle payment success
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        order_id = payment_intent['metadata']['order_id']
        
        try:
            order = Order.objects.get(id=order_id)
            order.status = 'processing'
            order.save()
        except Order.DoesNotExist:
            pass
    
    return HttpResponse(status=200)