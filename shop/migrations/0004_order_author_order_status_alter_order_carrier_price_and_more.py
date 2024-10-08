# Generated by Django 5.1 on 2024-08-12 21:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_method'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='carrier_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_cost_ttc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='taxe',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='shop.order'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='regular_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='solde_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='sub_total_ht',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='sub_total_ttc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='taxe',
            field=models.FloatField(),
        ),
    ]
