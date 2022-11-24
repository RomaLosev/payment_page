from django.db import models


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
        null=True,
        blank=True,
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
