# Generated by Django 4.2.1 on 2023-06-06 06:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_order_delivery_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotals',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
            preserve_default=False,
        ),
    ]
