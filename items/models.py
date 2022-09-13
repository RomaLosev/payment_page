from django.db import models


class Item(models.Model):
    name = models.CharField(
        help_text='Наименование товара',
        verbose_name='Наименование товара',
        max_length=255,
    )
    description = models.TextField(
        help_text='Описание товара',
        verbose_name='Описание товара',
    )
    price = models.PositiveSmallIntegerField(
        help_text='Цена товара',
        verbose_name='Цена товара',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(
        Item,
        related_name='Товары',
    )
    total_price = models.PositiveSmallIntegerField(
        help_text='Общая цена товаров в заказе',
        verbose_name='Цена товаров',
    )
