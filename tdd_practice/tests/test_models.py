from django.test import TestCase
from tdd_practice.models import Product


class ProductTestCase(TestCase):
    
    def setUp(self):
        self.product = Product.objects.create(name="tomate", price=23.50)

    def TestCreateProduct(self):
        product = Product.objects.get("tomate")
        self.assertEqual(product.name, "tomate")
        self.assertEqual(product.price, 23.50)
        
    def TestGetProduct(self):
        product = Product.objects.get(self.product.name)
        self.assertIsNotNone(product)
        self.assertEqual(self.product.name, product.name)
        self.assertEqual(self.product.price, product.price)
        