from django.test import TestCase
from .models import Card, expiration_date_func


class ExpirationDateTest(TestCase):

    def test_is_active_card(self):
        card = Card(series='test', number=123421424, expiration_date=expiration_date_func(-19), count=123, status=True)
        self.assertIs(card.is_active_card(), False)
