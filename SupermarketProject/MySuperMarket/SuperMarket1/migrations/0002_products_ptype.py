# Generated by Django 5.0.2 on 2024-02-11 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperMarket1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='ptype',
            field=models.CharField(max_length=100, null=True),
        ),
    ]