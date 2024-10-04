from django.urls import path
from rest_framework import routers

from .views import ProductView, RiskView, ProductMetaFieldView, CopyProductView, LOBView

app_name = 'app_products'

router = routers.SimpleRouter()
router.register('insurance_products', ProductView, basename='products')
router.register('risk_product', RiskView, basename='risk_product')
router.register('meta_field', ProductMetaFieldView, basename='meta_field')
router.register('lob', LOBView, basename='lob')


urlpatterns = [
    path('copy_product/', CopyProductView.as_view(), name='copy_product'),

]

urlpatterns += router.urls
