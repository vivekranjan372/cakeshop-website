# Generated by Django 3.1.2 on 2020-10-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeshop', '0005_registeruser_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_name', models.CharField(max_length=100)),
                ('cake_image', models.CharField(max_length=100)),
                ('cake_price', models.CharField(max_length=100)),
                ('addedUser', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'add_to_cart',
            },
        ),
    ]