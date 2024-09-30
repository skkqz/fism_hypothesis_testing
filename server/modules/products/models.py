import uuid

from django.db import models


class Product(models.Model):
    """
    Модель страхового продукта.
    """

    CHOICE_LOB = (
        ('CASCO', 'КАСКО'),
        ('OSAGO', 'ОСАГО'),
        ('THI', 'Страхование путешественников'),
        ('ACCIDENT', 'Страхование от несчастных случаев'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    risk = models.ManyToManyField('Risk', through='ProductRisk', related_name='products',
                                  verbose_name='Риски продукта')
    name = models.CharField(max_length=500, verbose_name='Наименование продукта')
    lob = models.CharField(max_length=500, choices=CHOICE_LOB, default='CASCO', blank=False, null=True, verbose_name='Линия бизнеса')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Risk(models.Model):
    """
    Модель рисков продукта.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500, blank=False, verbose_name='Наименование риска')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Риск'
        verbose_name_plural = 'Риски'

    def __str__(self):
        return self.name


class ProductMetaField(models.Model):
    """
    Модель для хранения дополнительных метаданных, связанных с конкретным страховым продуктом.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='meta_fields', verbose_name='Продукт')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    value = models.CharField(max_length=500, verbose_name='Значения поля')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Мета поле'
        verbose_name_plural = 'Мета поля'

    def __str__(self):
        return self.name


class ProductRisk(models.Model):
    """
    Промежуточная модель продукта и рисков.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name='product_risks', on_delete=models.CASCADE)
    risk = models.ForeignKey(Risk, related_name='risk_products', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт - Риск'
        verbose_name_plural = 'Продукты - Риски'

    def __str__(self):
        return f'{self.product} - {self.risk}'
