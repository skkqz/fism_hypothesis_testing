from itertools import product

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Product, Risk, ProductMetaField, LOB
from .service import CopyProduct


copy_product = CopyProduct()
COPY_PREFIX = '(КОПИЯ)'



class LOBSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для хранения информации о линии бизнеса.
    """

    class Meta:
        model = LOB
        fields = ('id', 'name')

    def to_representation(self, instance):
        response = super().to_representation(instance)

        meta_fields = ProductMetaField.objects.filter(lob=instance)
        response['meta_fields'] = ProductMetaFieldSerializer(meta_fields, many=True).data

        return response

class LOBForProductSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для хранения информации о линии бизнеса.
    """

    class Meta:
        model = LOB
        fields = ('id', 'name')


class ProductMetaFieldSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для хранения дополнительных метаданных, связанных с конкретным страховым продуктом.
    """

    lob = serializers.PrimaryKeyRelatedField(queryset=LOB.objects.all(), label='Линия бизнеса')

    class Meta:
        model = ProductMetaField
        fields = ('id', 'name', 'lob', 'risks', 'updated_at', 'created_at')
        read_only_fields = ('created_at','updated_at',)


    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['risks'] = RiskSerializer(instance.risks.all(), many=True).data

        return response


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для страхового продукта.
    """

    risks = serializers.PrimaryKeyRelatedField(queryset=Risk.objects.all(), many=True, required=True, label='Риски продукта')

    class Meta:
        model = Product
        fields = ('id', 'name', 'lob', 'risks')
        read_only_fields = ('created_at','updated_at', )

    def to_representation(self, instance):

        response = super().to_representation(instance)
        response['lob'] = LOBForProductSerializer(instance.lob).data
        response['risks'] = RiskSerializer(instance.risks.all(), many=True).data

        return response


class RiskSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для страховых рисков.
    """

    class Meta:
        model = Risk
        fields = ('id', 'name', 'rate', 'value', 'updated_at', 'created_at')
        read_only_fields = ('created_at','updated_at',)


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
        product = get_object_or_404(Product, pk=pk)
        
        copy_product.copy_all_product(product)

        return validated_data

    def update(self, instance, validated_data):
        raise NotImplemented('Метод не реализован.')