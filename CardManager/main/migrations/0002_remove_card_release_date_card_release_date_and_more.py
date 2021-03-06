# Generated by Django 4.0.6 on 2022-07-17 21:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='Release_date',
        ),
        migrations.AddField(
            model_name='card',
            name='release_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='card',
            name='expiration_date',
            field=models.DateField(default=main.models.expiration_six_month),
        ),
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('APPLE', 'an apple'), ('ORANGE', 'orange')], max_length=30)),
                ('price', models.IntegerField()),
                ('buy_date', models.DateTimeField(auto_now=True)),
                ('card_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.card')),
            ],
        ),
    ]
