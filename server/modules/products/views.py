from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .mixins import AtomicMixin
from .models import Product, Risk, ProductMetaField, LOB
from . serializer import (ProductSerializer, ProductMetaFieldSerializer, RiskSerializer, CopyProductSerializer,
                          LOBSerializer)


class ProductView(AtomicMixin, ModelViewSet):
    """
    Представление для продукта.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class RiskView(AtomicMixin, ModelViewSet):
    """
    Представление для рисков продукта.
    """

    queryset = Risk.objects.all()
    serializer_class = RiskSerializer
    permission_classes = [IsAuthenticated]


class ProductMetaFieldView(AtomicMixin, ModelViewSet):
    """
    Представление для мета данных продукта.
    """

    queryset = ProductMetaField.objects.all()
    serializer_class = ProductMetaFieldSerializer
    permission_classes = [IsAuthenticated]


class LOBView(AtomicMixin, ModelViewSet):
    """
    Представление для линии бизнеса.
    """

    queryset = LOB.objects.all()
    serializer_class = LOBSerializer
    permission_classes = [IsAuthenticated]


class CopyProductView(AtomicMixin ,CreateAPIView):
    """
    Представление для копирования продукта.
    """

    queryset = Product.objects.all()
    serializer_class = CopyProductSerializer
    permission_classes = [IsAuthenticated]
