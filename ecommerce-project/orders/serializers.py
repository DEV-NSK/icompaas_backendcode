from rest_framework import serializers
from .models import Order, OrderItem, Cart, CartItem
from products.serializers import ProductListSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    total_price = serializers.ReadOnlyField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price', 'created_at', 'updated_at']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_number', 'user', 'total_amount', 'created_at', 'updated_at']

class CreateOrderSerializer(serializers.Serializer):
    shipping_address = serializers.CharField()
    billing_address = serializers.CharField(required=False)
    
    def validate(self, attrs):
        user = self.context['request'].user
        cart = user.cart
        
        if not cart.items.exists():
            raise serializers.ValidationError("Cart is empty")
        
        return attrs