from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Avg, Case, When, Value, FloatField
from .models import Product, Category, Review, ProductImage
from .serializers import ProductSerializer, ProductListSerializer, CategorySerializer, ReviewSerializer, ProductImageSerializer, ProductCreateSerializer

class CategoryList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'featured']
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price', 'created_at', 'name']
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        
        # Price range filter
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
            
        # Category filter with multiple values
        categories = self.request.query_params.getlist('category')
        if categories:
            queryset = queryset.filter(category_id__in=categories)
            
        return queryset

class ProductDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.filter(active=True)
    serializer_class = ProductSerializer

class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(id=product_id)
        
        # Check if user already reviewed this product
        if Review.objects.filter(product=product, user=self.request.user).exists():
            raise serializers.ValidationError("You have already reviewed this product.")
        
        serializer.save(user=self.request.user, product=product)

class ReviewList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return Review.objects.filter(product_id=product_id).order_by('-created_at')

class ReviewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    
    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

# Add this new view for image uploads
class ProductImageCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductImageSerializer
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(id=product_id)
        serializer.save(product=product)

class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    # serializer_class = ProductSerializer
    serializer_class = ProductCreateSerializer  # Use the new serializer
    
    def perform_create(self, serializer):
        # Only staff/admin users can create products
        if not self.request.user.is_staff:
            raise serializers.ValidationError("Only staff members can create products.")
        serializer.save()

class ProductUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCreateSerializer #ProductSerializer
    queryset = Product.objects.all()
    
    def get_queryset(self):
        # Only staff can update/delete products
        if self.request.user.is_staff:
            return Product.objects.all()
        return Product.objects.none()