# Generated by Django 4.1.1 on 2022-09-14 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_price_remove_item_price_delete_order_price_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_price_id', models.CharField(help_text='Цена товара в stripe', max_length=100)),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='Цена товара в центах'),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.AddField(
            model_name='stripeprice',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item'),
        ),
    ]
