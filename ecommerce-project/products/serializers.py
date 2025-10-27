# products/serializers.py
from rest_framework import serializers
from django.db.models import Avg
from .models import Category, Product, ProductImage, Review
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'title', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['user']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False},
        }
    
    def get_average_rating(self, obj):
        return obj.reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    def get_review_count(self, obj):
        return obj.reviews.count()

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'compare_price', 'category', 'image', 'stock', 'featured', 'active']
        extra_kwargs = {
            'image': {'required': False},
        }

class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'compare_price', 'category', 'image', 
                 'average_rating', 'review_count', 'featured', 'created_at']
    
    def get_average_rating(self, obj):
        return obj.reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    def get_review_count(self, obj):
        return obj.reviews.count()