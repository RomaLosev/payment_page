from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from items.models import Item

User = get_user_model()


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(
        Item,
        verbose_name='Товары',
        related_name='ordered',
        through='ItemInOrder',
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_absolute_url(self) -> str:
        return f'/order/{self.id}'

    def __str__(self) -> str:
        return f'Заказ №{self.id}'


class ItemInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
    )
    item = models.ForeignKey(
        Item,
        verbose_name='наименование',
        on_delete=models.CASCADE,
        related_name='order',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        default=1,
        validators=(
            MinValueValidator(1),
        )
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return f'{self.item.name} в заказе {self.order.id}'


class Discount(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    percentage = models.PositiveIntegerField(
        verbose_name='Размер скидки',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(99),
        ),
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='discount',
    )

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self) -> str:
        return f'{self.name}: {self.percentage}%'


class Tax(models.Model):
    name = models.CharField(
        verbose_name='Налог',
        max_length=150,
    )
    inclusive = models.BooleanField(
        verbose_name='Налог включен в стоимость',
        default=False,
    )
    percentage = models.PositiveIntegerField(
        verbose_name='Размер налога',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99)
        ],
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='tax',
    )

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self) -> str:
        return f'{self.name}: {self.percentage}%'
