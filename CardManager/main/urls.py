from django.urls import path
from .views import *


urlpatterns = [
    path('', CardListView.as_view(), name='home'),
    path('card/<int:card_id>/', CardDetailView.as_view(), name='card'),
    path('delete/<int:card_id>', card_delete, name='delete'),
]
