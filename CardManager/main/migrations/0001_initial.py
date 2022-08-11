# Generated by Django 4.0.6 on 2022-08-11 15:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('release_date', models.DateField(default=datetime.date.today)),
                ('expiration_date', models.DateField(default=main.models.expiration_six_month)),
                ('date_of_use', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(null=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('APPLE', 'an apple'), ('ORANGE', 'orange')], max_length=30)),
                ('price', models.IntegerField()),
                ('buy_date', models.DateTimeField(auto_now=True)),
                ('card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.card')),
            ],
        ),
    ]
