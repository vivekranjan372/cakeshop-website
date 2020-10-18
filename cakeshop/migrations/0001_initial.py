# Generated by Django 3.1.2 on 2020-10-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cake_user',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'test_register',
            },
        ),
        migrations.CreateModel(
            name='SellCake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_name', models.CharField(max_length=100)),
                ('cake_image', models.ImageField(default='', upload_to='static/images')),
                ('cake_description', models.CharField(max_length=100)),
                ('cake_ingredients', models.CharField(max_length=100)),
                ('cake_method', models.CharField(max_length=100)),
                ('uploader_id', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'cake_details',
            },
        ),
    ]