from typing import Dict

from .models import Product, Risk, ProductMetaField, LOB


class CopyProduct:
    """
    Класс копирования продукта.
    """

    def __init__(self):
        self.copy_risks = CopyRisk()
        self.copy_product_meta_field = CopyLOB()


    def copy_all_product(self, product: Product) -> Product:
        """
        Полное копирования продукта.

        :param product: Продукт для копирования.
        :return: Созданная полная копия продукта.
        """

        copy_product = self.copy_product(product)
        self.copy_risks.copy_risk(new_product=copy_product, old_product=product)
        self.copy_product_meta_field.copy_meta_field(new_product=copy_product, old_product=product)

        return copy_product

    @staticmethod
    def copy_product(product: Product) -> Product:
        """
        Создание копии продукта.

        :param product: Продукт для копирования.
        :return: Созданная копия продукта.
        """

        new_name = f'{product.name} (КОПИЯ)'
        new_product = Product.objects.create(
            name=new_name,
            lob=product.lob
        )

        return new_product


class CopyRisk:
    """
    Класс копирования рисков.
    """

    @staticmethod
    def copy_risk(old_product: Product, new_product: Product) -> Product:

        risks = old_product.risks.all()
        new_product.risks.set(risks)
        new_product.save()

        return new_product


class CopyLOB:
    """
    Копирования мета полей продукта.
    """

    @staticmethod
    def copy_meta_field(old_product: Product, new_product: Product) -> Product:

        new_product.lob = old_product.lob
        new_product.save()

        return new_product
