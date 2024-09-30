from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product, Risk, ProductMetaField


@admin.register(Product)
class ProductAdmin(ModelAdmin):

    list_display = ['name', 'lob']


@admin.register(Risk)
class RiskAdmin(ModelAdmin):
    list_display = ['name']


@admin.register(ProductMetaField)
class ProductMetaFieldAdmin(ModelAdmin):
    list_display = ['name', 'value']