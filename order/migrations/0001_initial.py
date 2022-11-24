# Generated by Django 4.1.3 on 2022-11-24 11:16

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0005_remove_discount_order_remove_iteminorder_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='items.item')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Налог')),
                ('inclusive', models.BooleanField(default=False, verbose_name='Налог включен в стоимость')),
                ('percentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='Размер налога')),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(related_name='ordered', through='order.ItemInOrder', to='items.item', verbose_name='Товары')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='iteminorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order'),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('percentage', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='Размер скидки')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount', to='order.order')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
    ]