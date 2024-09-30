from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient

from .models import Product, Risk
import uuid


User = get_user_model()

class ProductViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@qwe.com', password='testpassword')
        self.client.login(email='testuser@qwe.com', password='testpassword')
        self.risk = Risk.objects.create(id=uuid.uuid4(), name="Test Risk")
        self.product = Product.objects.create(id=uuid.uuid4(), name="Test Product", lob="CASCO")
        self.product.risk.add(self.risk)

    def test_get_products(self):
        """
        Тест получения списка продуктов.
        """

        url = reverse('products:products-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        """
        Тест создания нового продукта.
        """

        url = reverse('products:products-list')

        data = {
            "name": "New Product",
            "lob": "OSAGO",
            "risk": [self.risk.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(name="New Product").lob, "OSAGO")

    def test_get_product_detail(self):
        """
        Тест детального отображения продукта.
        """

        url = reverse('products:products-detail', args=[self.product.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Test Product")
        self.assertEqual(response.data['lob'], "CASCO")
        self.assertEqual(response.data['risk'][0]['id'], str(self.risk.id))