from django.test import TestCase
from .models import Card, expiration_date_func


class ExpirationDateTest(TestCase):

    def test_is_active_card(self):
        card = Card(series='test', number=123421424, expiration_date='2021-10-25 14:30:59', count=123, status=True)
        self.assertIs(card.)
