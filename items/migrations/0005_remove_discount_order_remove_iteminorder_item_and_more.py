# Generated by Django 4.1.3 on 2022-11-24 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_iteminorder_tax_item_currency_alter_item_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='order',
        ),
        migrations.RemoveField(
            model_name='iteminorder',
            name='item',
        ),
        migrations.RemoveField(
            model_name='iteminorder',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.DeleteModel(
            name='Tax',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='ItemInOrder',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
