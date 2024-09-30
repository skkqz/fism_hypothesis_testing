import uuid
from django.db import models


class Division(models.Model):
    """
    Модель подразделения агента.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, verbose_name='Наименования подразделения')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name


class Face(models.Model):
    """
    Модель контрагента.
    """

    CHOICE_COUNTERPARTY = (
        ('NATURAL', 'Физическое лицо'),
        ('LEGAl', 'Юридическое лицо'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    counterparty_type = models.CharField(max_length=255, choices=CHOICE_COUNTERPARTY, default='NATURAL', blank=False, verbose_name='Тип контрагента')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Отчество')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    data_birth = models.DateField(verbose_name='Дата рождения')
    name_legal_entity = models.CharField(max_length=255, verbose_name='Наименования юридического лица')
    inn = models.IntegerField(verbose_name='ИНН')
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self):
        return self.first_name



class Agent(models.Model):
    """
    Модель агента.
    """

    CHOICE_STATUS = (
        ('PROJECT', 'Проект'),
        ('WORKS', 'Работает'),
        ('COMPLETED', 'Завершен'),
        ('TERMINATED', 'Расторгнут'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    face = models.ForeignKey(Face, on_delete=models.CASCADE, blank=False, verbose_name='Контрагент')
    division = models.ForeignKey(Division, on_delete=models.CASCADE, blank=False, verbose_name='Подразделение') # OneToOne
    status = models.CharField(max_length=255, choices=CHOICE_STATUS, blank=False, verbose_name='Статус агентского договора')
    created_at = models.DateField(auto_now_add=True, blank=False, verbose_name='Дата создания договора')
    date_begin = models.DateField(verbose_name='Дата начала действия')
    date_end = models.DateField(verbose_name='Дата окончания действия')

    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'

    def __str__(self):
        return self.status
