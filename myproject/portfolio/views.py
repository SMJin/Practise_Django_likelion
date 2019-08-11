from django.shortcuts import render, get_object_or_404, redirect

from .models import Portfolio

def portfolio(request):
    portfolios = Portfolio.objects 
    return render(request, 'portfolio/portfolio.html', {'portfolios' : portfolios})

def new(request):
    return render(request, 'portfolio/new.html')

def create(request):
    portfolios = Portfolio()
    portfolios.title = request.GET['title']
    portfolios.image = request.GET['image']
    portfolios.description = request.GET['description']
    portfolios.save()
    return redirect('/portfolio/')

def delete(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    portfolio.delete()
    return redirect('/portfolio/')

