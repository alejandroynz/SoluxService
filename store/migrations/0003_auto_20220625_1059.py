# Generated by Django 3.1.4 on 2022-06-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220603_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
    ]
