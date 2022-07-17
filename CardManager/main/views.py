from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Q


class CardListView(ListView):
    model = Card
    template_name = 'main/list.html'
    context_object_name = 'cards'
    allow_empty = True
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список карт'
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Card.objects.filter(
                Q(series__icontains=query) | Q(number__icontains=query)
            )
            return object_list
        else:
            return Card.objects.all()


class CardDetailView(DetailView):
    model = Card
    template_name = 'main/detail.html'
    pk_url_kwarg = 'card_id'
    context_object_name = 'card'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['card'].status
        return context
