# Generated by Django 3.1.2 on 2020-10-15 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeshop', '0003_sellcake_cake_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellandbuy',
            name='cake_price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='sellandbuy',
            name='delivery_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sellandbuy',
            name='payment_method',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sellandbuy',
            name='user_type',
            field=models.CharField(default='', max_length=20),
        ),
    ]