from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Product, Risk, ProductMetaField
from . serializer import ProductSerializer, ProductMetaFieldSerializer, RiskSerializer, CopyProductSerializer


class ProductView(ModelViewSet):
    """
    Представление для продукта.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class RiskView(ModelViewSet):
    """
    Представление для рисков продукта.
    """

    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    permission_classes = [IsAuthenticated]


class ProductMetaFieldView(ModelViewSet):
    """
    Представление для мета данных продукта.
    """

    queryset = ProductMetaField.objects.all()
    serializer_class = ProductMetaFieldSerializer
    permission_classes = [IsAuthenticated]


class CopyProductView(CreateAPIView):
    """
    Представление для копирования продукта.
    """

    queryset = Product.objects.all()
    serializer_class = CopyProductSerializer
    permission_classes = [IsAuthenticated]
