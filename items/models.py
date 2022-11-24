from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class Item(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'usd'),
        ('EUR', 'eur'),
    ]
    name = models.CharField(
        help_text='Наименование товара',
        verbose_name='Наименование товара',
        max_length=255,
    )
    description = models.TextField(
        help_text='Описание товара',
        verbose_name='Описание товара',
    )
    price = models.PositiveIntegerField(
        help_text='Цена товара в центах',
        verbose_name='Цена',
        default=0,
    )
    currency = models.CharField(
        verbose_name='Валюта',
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='USD',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_price(self) -> str:
        return "{0:.2f}".format(self.price / 100)

    def get_absolute_url(self):
        return f'/item/{self.id}'

    def __str__(self):
        return self.name


class StripePrice(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )
    stripe_price_id = models.CharField(
        max_length=200,
        help_text='Цена товара в stripe',
    )

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return self.stripe_price_id


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

    def get_absolute_url(self):
        return f'/order/{self.id}'

    def __str__(self):
        return f'Заказ №{self.id}'


class ItemInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='order',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество',
        default=1,
    )

    def __str__(self):
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

    def __str__(self):
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

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self):
        return f'{self.name}: {self.percentage}%'
