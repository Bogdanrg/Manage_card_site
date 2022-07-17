from django.db import models
from django.urls import reverse
import datetime


def expiration_func():
    date_now = datetime.date.today()
    month = date_now.month
    date_expiration = date_now.replace(month=month+3)
    return date_expiration


class Card(models.Model):
    series = models.CharField(max_length=30)
    number = models.IntegerField()
    release_date = models.DateField(default=datetime.date.today)
    expiration_date = models.DateField(default=expiration_func)
    date_of_use = models.DateTimeField(auto_now=True)
    count = models.IntegerField(null=True)
    status = models.BooleanField()

    def __str__(self):
        return self.series

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})


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
    card_id = models.ForeignKey('Card', on_delete=models.PROTECT)
