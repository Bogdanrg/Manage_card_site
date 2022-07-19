from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['card_id'].empty_label = 'Карта не выбрана'

    class Meta:
        model = Purchase
        fields = ['product', 'price', 'card_id']
