# Generated by Django 5.0.2 on 2024-02-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperMarket1', '0002_products_ptype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='exp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='mfd',
            field=models.DateTimeField(),
        ),
    ]
