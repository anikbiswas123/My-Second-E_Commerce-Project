# Generated by Django 4.1.7 on 2023-04-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Discount_Price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
