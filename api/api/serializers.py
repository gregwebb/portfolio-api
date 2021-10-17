from rest_framework import serializers, views
from .models import Portfolio,User,Holding,Allocation
import yfinance as yf
from decimal import Decimal


class HoldingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Holding
        fields = ('ticker', 'quantity', 'asset_class', 'sector')

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    portfolio_value = serializers.SerializerMethodField()
    sectors_held = serializers.SerializerMethodField()
    def get_portfolio_value(self, object):
        tickers = Holding.objects.filter(portfolio_id=object.id)
        portfolio_value = 0
        for x in tickers:
            ticker = yf.Ticker(x.ticker)
            todays_data = ticker.history(period='1d')
            price = todays_data['Close'][0]
            portfolio_value = portfolio_value + float(x.quantity)*price
        portfolio = Portfolio.objects.get(id=object.id)
        portfolio.portfolio_value = portfolio_value
        portfolio.save()
        return "$%.2f" % round(portfolio_value,2)



    def get_sectors_held(self, object):
        information_technology_holdings = Holding.objects.filter(portfolio_id=object.id,sector="Information Technology")
        information_technology_value = 0
        for x in information_technology_holdings:
            ticker = yf.Ticker(x.ticker)
            todays_data = ticker.history(period='1d')
            price = todays_data['Close'][0]
            information_technology_value = information_technology_value + float(x.quantity)*price
        information_technology_weight = Decimal(information_technology_value)/object.portfolio_value

        health_care_holdings = Holding.objects.filter(portfolio_id=object.id,sector="Health Care")
        health_care_value = 0
        for x in health_care_holdings:
            ticker = yf.Ticker(x.ticker)
            todays_data = ticker.history(period='1d')
            price = todays_data['Close'][0]
            health_care_value = health_care_value + float(x.quantity)*price
        health_care_weight = Decimal(health_care_value)/object.portfolio_value

        financial_holdings = Holding.objects.filter(portfolio_id=object.id,sector="Financials")
        financial_value = 0
        for x in financial_holdings:
            ticker = yf.Ticker(x.ticker)
            todays_data = ticker.history(period='1d')
            price = todays_data['Close'][0]
            financial_value = financial_value + float(x.quantity)*price
        financial_weight = Decimal(financial_value)/object.portfolio_value



        return "Information Technology", round(information_technology_weight,2), "Health Care", round(health_care_weight,2), "Financials", round(financial_weight,2)


    class Meta:
        model = Portfolio
        fields = ('name', 'allocation_id', 'order', 'portfolio_value', 'sectors_held')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    portfolios = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'risk_profile', 'portfolios')
    def get_portfolios(self, object):
        portfolios = Portfolio.objects.filter(user_id=object.id)
        return PortfolioSerializer(portfolios, many=True).data

class AllocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allocation
        fields = ('sector1', 'sector2', 'sector3', 'sector4', 'sector5', 'sector6', 'sector7', 'sector8', 'sector9', 'sector10', 'sector11', 'sector12', 'sector13')
