from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product, Risk, ProductMetaField, LOB, ProductRisk


@admin.register(Product)
class ProductAdmin(ModelAdmin):

    list_display = ['name', 'lob']


@admin.register(Risk)
class RiskAdmin(ModelAdmin):
    list_display = ['name']


@admin.register(ProductMetaField)
class ProductMetaFieldAdmin(ModelAdmin):
    list_display = ['name', 'lob']


@admin.register(LOB)
class LOBAdmin(ModelAdmin):
    list_display = ['name',]


@admin.register(ProductRisk)
class ProductRiskAdmin(ModelAdmin):
    list_display = ['product', 'risk']