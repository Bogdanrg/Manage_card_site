# Generated by Django 4.0.6 on 2022-10-29 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 30, 1, 9, 14, 985006)),
        ),
    ]
