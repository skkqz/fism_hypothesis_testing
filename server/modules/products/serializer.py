from tabnanny import check

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Product, Risk, ProductMetaField
from .service import CopyProduct


copy_product = CopyProduct()
COPY_PREFIX = '(КОПИЯ)'


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для страхового продукта.
    """

    risk = serializers.PrimaryKeyRelatedField(queryset=Risk.objects.all(), many=True, label='Риски')

    class Meta:
        model = Product
        fields = ('id', 'name', 'lob', 'risk')
        read_only_fields = ('created_at','updated_at', )


    def create(self, validated_data):

        return super().create(validated_data)

    def update(self, instance, validated_data):

        return super().update(instance, validated_data)

    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['risk'] = RiskSerializer(instance.risk.all(), many=True).data
        response['meta_fields'] = ProductMetaFieldSerializer(instance.meta_fields.all(), many=True).data

        return response


class RiskSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для страховых рисков.
    """

    class Meta:
        model = Risk
        fields = ('id', 'name', 'updated_at', 'created_at')
        read_only_fields = ('created_at','updated_at',)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return super().to_representation(instance)


class ProductMetaFieldSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для хранения дополнительных метаданных, связанных с конкретным страховым продуктом.
    """

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), label='Продукт')

    class Meta:
        model = ProductMetaField
        fields = ('id', 'name', 'value', 'product', 'updated_at', 'created_at')
        read_only_fields = ('created_at','updated_at',)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return super().to_representation(instance)


class CopyProductSerializer(serializers.Serializer):
    """
    Сериалайзер для копирования продукта.
    """

    copy_product_id = serializers.UUIDField(label='id продукта копирования')

    def validate(self, attrs):

        pk = attrs.get('copy_product_id', None)
        product = get_object_or_404(Product, pk=pk)

        check_name_copy = Product.objects.filter(name__startswith=f'{product.name} (КОПИЯ)')

        if check_name_copy.exists():
            raise serializers.ValidationError({'detail': 'Создать можно только одну копию.'})


        return attrs

    def create(self, validated_data):

        pk = validated_data['copy_product_id']

        product =get_object_or_404(Product, pk=pk)

        copy_product.copy_all_product(product)

        return validated_data

    def update(self, instance, validated_data):
        raise NotImplemented('Метод не реализован.')