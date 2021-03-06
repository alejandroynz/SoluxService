# Generated by Django 3.1.4 on 2022-07-02 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20220701_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_paid',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
    ]
