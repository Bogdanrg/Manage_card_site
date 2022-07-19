from django.db import models
from django.urls import reverse
import datetime


def expiration_six_month():
    date_now = datetime.date.today()
    month = date_now.month
    date_expiration = date_now.replace(month=month+3)
    return date_expiration


class Card(models.Model):
    series = models.CharField(max_length=30)
    number = models.IntegerField()
    release_date = models.DateField(default=datetime.date.today)
    expiration_date = models.DateField(default=expiration_six_month)
    date_of_use = models.DateTimeField(auto_now=True)
    count = models.IntegerField(null=True)
    status = models.BooleanField()

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})

    def get_delete_absolute_url(self):
        return reverse('delete', kwargs={'card_id': self.pk})


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

#for i in range(10):
...     #dict={}
...     #dict['series'] = 'third'
...     #dict['number'] = randrange(10101010, 98989898)
...     #dict['count'] = randrange(10, 500)
...     #dict['status'] = True
...     #Card.objects.create(**dict)
#