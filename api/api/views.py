from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic.detail import DetailView
from .serializers import PortfolioSerializer,UserSerializer, HoldingSerializer, AllocationSerializer
from .models import Portfolio,User,Holding,Allocation
from django.http import HttpResponse
from decimal import Decimal
import yfinance as yf

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all().order_by('id')
    serializer_class = PortfolioSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class HoldingViewSet(viewsets.ModelViewSet):
    queryset = Holding.objects.all().order_by('id')
    serializer_class = HoldingSerializer

class AllocationViewSet(viewsets.ModelViewSet):
    queryset = Allocation.objects.all().order_by('id')
    serializer_class = AllocationSerializer

def current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]

def portfolio_view(request, id, *args, **kwargs):
    obj = Portfolio.objects.get(id=id)
    tickers = Holding.objects.filter(portfolio=id)
    ticker_list = [x.ticker for x in tickers]

    portfolio_value = 0
    for x in tickers:
        portfolio_value = portfolio_value + float(x.quantity)*current_price(x.ticker)
        x.value = float(x.quantity)*current_price(x.ticker)

    ticker_values = [x.value for x in tickers]

    information_technology_holdings = Holding.objects.filter(portfolio=id,sector="Information Technology")
    information_technology_value = 0
    for x in information_technology_holdings:
        information_technology_value = information_technology_value + float(x.quantity)*current_price(x.ticker)
    information_technology_weight = information_technology_value/portfolio_value


    return HttpResponse(f"<h1>Portfolio ID: {id} <br> Portfolio Name: {obj.name} <br> <br> Holdings: {ticker_list} <br> Holding Values: {ticker_values} <br> Portfolio Value: {portfolio_value}  <br><br> Information Technology Value: {information_technology_value} <br> Information Technology Sector Weight: {information_technology_weight} <br> Information Technology Target Weight: {obj.allocation.sector1}</h1>")
