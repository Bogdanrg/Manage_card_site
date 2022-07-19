from django.http import HttpResponse
from django.shortcuts import render, redirect
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
        context['title'] = 'Cards'
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
        context['title'] = f'Card - {context["card"].pk}'
        context['card_id'] = context['card'].pk
        return context

    def post(self, request, *args, **kwargs):
        card_id = self.kwargs.get('card_id')
        card = Card.objects.get(pk=card_id)
        if card.status:
            Card.objects.filter(pk=card_id).update(status=False)
        else:
            Card.objects.filter(pk=card_id).update(status=True)
        return redirect('card', card_id=card_id)


def card_delete(request, card_id):
    Card.objects.filter(pk=card_id).delete()
    return redirect('home')
