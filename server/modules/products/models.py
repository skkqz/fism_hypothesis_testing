import uuid

from django.db import models


class LOB(models.Model):
    """
    Модель для хранения информации о линии бизнеса.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500, verbose_name='Наименование линии бизнеса')
    risks = models.ManyToManyField('Risk', related_name='lobs', verbose_name='Риски метаполя')


    class Meta:
        verbose_name = 'Линия бизнеса'
        verbose_name_plural = 'Линии бизнеса'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель страхового продукта.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500, verbose_name='Наименование продукта')
    lob = models.ForeignKey(LOB, on_delete=models.CASCADE, blank=False, null=True, verbose_name='Линия бизнеса')
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
    value = models.IntegerField(verbose_name='Сумма страхования по данному риску')
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
    lob = models.ForeignKey(LOB, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Линия бизнеса')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    is_required = models.BooleanField(default=False, verbose_name='Обязательное/Не обязательно поле')
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
