# Generated by Django 5.0.2 on 2024-02-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperMarket1', '0003_alter_products_exp_alter_products_mfd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='exp',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='mfd',
            field=models.DateField(),
        ),
    ]
