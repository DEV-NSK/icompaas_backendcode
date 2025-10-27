from django.core.management.base import BaseCommand
from products.models import Category, Product, ProductImage
from django.contrib.auth import get_user_model
import os
from django.core.files import File

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Create categories
        electronics = Category.objects.create(
            name='Electronics',
            description='Latest electronic gadgets and devices'
        )
        
        clothing = Category.objects.create(
            name='Clothing',
            description='Fashionable clothing for everyone'
        )
        
        books = Category.objects.create(
            name='Books',
            description='Books for all ages and interests'
        )
        
        home = Category.objects.create(
            name='Home & Garden',
            description='Items for your home and garden'
        )
        
        # Create sample products
        products_data = [
            {
                'name': 'Wireless Bluetooth Headphones',
                'description': 'High-quality wireless headphones with noise cancellation',
                'price': 99.99,
                'compare_price': 129.99,
                'category': electronics,
                'stock': 50,
                'featured': True
            },
            {
                'name': 'Smartphone X',
                'description': 'Latest smartphone with advanced features',
                'price': 699.99,
                'compare_price': 799.99,
                'category': electronics,
                'stock': 30,
                'featured': True
            },
            {
                'name': 'Cotton T-Shirt',
                'description': 'Comfortable 100% cotton t-shirt',
                'price': 19.99,
                'category': clothing,
                'stock': 100,
                'featured': False
            },
            {
                'name': 'Programming Book: Python Mastery',
                'description': 'Comprehensive guide to Python programming',
                'price': 29.99,
                'category': books,
                'stock': 25,
                'featured': True
            },
            {
                'name': 'Garden Tool Set',
                'description': 'Complete set of gardening tools',
                'price': 49.99,
                'compare_price': 59.99,
                'category': home,
                'stock': 15,
                'featured': False
            },
        ]
        
        for product_data in products_data:
            product = Product.objects.create(**product_data)
            self.stdout.write(f'Created product: {product.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully seeded database with sample data!')
        )