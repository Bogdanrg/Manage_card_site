from django.db import models, connection
from django.utils import timezone
from django.urls import reverse
import datetime
from random import randrange


def expiration_date_func(days):
    date_now = datetime.datetime.now()
    expiration_date = date_now + datetime.timedelta(days=days)
    return expiration_date


class Card(models.Model):
    series = models.CharField(max_length=30)
    number = models.IntegerField()
    release_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    date_of_use = models.DateTimeField(null=True)
    count = models.IntegerField(null=True)
    status = models.BooleanField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.release_date = timezone.now()
        self.date_of_use = timezone.now()
        return super(Card, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})

    def get_delete_absolute_url(self):
        return reverse('delete', kwargs={'card_id': self.pk})


def create_cards():
    for obj in range(10):
        with connection.cursor() as cursor:
            cursor.execute("insert into main_card(series, number, expiration_date, count, status)"
                           "values('BlackSeria', 781232312899, '2026-10-25 14:30:59', 100, 1)")


class Purchase(models.Model):
    APPlE = 'APPLE'
    ORANGE = 'ORANGE'
    PRODUCTS_LIST = [
        (APPlE, 'an apple'),
        (ORANGE, 'orange'),
    ]
    product = models.CharField(max_length=30, choices=PRODUCTS_LIST)
    price = models.IntegerField()
    buy_date = models.DateTimeField(auto_now=True)
    card_id = models.ForeignKey('Card', on_delete=models.CASCADE)
