# Generated by Django 4.0.6 on 2022-10-30 11:51

from django.db import migrations, models
import django.db.models.deletion


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
                ('release_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('date_of_use', models.DateTimeField(null=True)),
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
