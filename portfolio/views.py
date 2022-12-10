from django.shortcuts import render, get_object_or_404

from .models import Portfolio

def index(request):
    portfolio = Portfolio.objects
    context = {'portfolio': portfolio}
    return render(request, 'index.html', context)

def detail(request, id):
    detail = get_object_or_404(Portfolio, pk=id)
    context = {'portfolio': detail}
    return render(request, 'detail.html', context)