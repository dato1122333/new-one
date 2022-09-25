# Generated by Django 4.0.6 on 2022-09-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('owner_phone', models.CharField(max_length=9, verbose_name="Owner's Phone Number")),
                ('client_phone', models.CharField(max_length=9, verbose_name="Client's Phone Number")),
                ('my_date', models.CharField(max_length=13, verbose_name='exact Date')),
                ('my_time', models.CharField(max_length=5, verbose_name='exact Time')),
            ],
        ),
    ]
