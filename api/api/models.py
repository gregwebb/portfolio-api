from django.db import models
from decimal import Decimal

class RiskProfile(models.TextChoices):
    AGGRESSIVE = ('Aggressive')
    BALANCED = ('Balanced')
    CONSERVATIVE = ('Conservative')

class AssetClass(models.TextChoices):
    EQUITIES = ('Equities')
    FIXED_INCOME = ('Fixed Income')
    CASH = ('Cash / Cash Equivalent')
    CRYPTOCURRENCY = ('Cryptocurrency')

class Sector(models.TextChoices):
    INFORMATION_TECHNOLOGY = ('Information Technology')
    HEALTH_CARE = ('Health Care')
    FINANCIAL = ('Financials')
    CONSUMER_DISCRETIONARY = ('Consumer Discretionary')
    COMMUNICATION_SERVICES = ('Communication Services')
    INDUSTIALS = ('Industrials')
    CONSUMER_STAPLES = ('Consumer Staples')
    ENERGY = ('Energy')
    UTILITIES = ('Utilities')
    REAL_ESTATE = ('Real Estate')
    MATERIALS = ('Materials')
    CASH = ('Cash')
    OTHER = ('Other')

class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    risk_profile = models.CharField(
        max_length = 60,
        choices = RiskProfile.choices,
        default = RiskProfile.AGGRESSIVE,
    )

class Allocation(models.Model):
    sector1 = models.DecimalField(max_digits=4,decimal_places=4)
    sector2 = models.DecimalField(max_digits=4,decimal_places=4)
    sector3 = models.DecimalField(max_digits=4,decimal_places=4)
    sector4 = models.DecimalField(max_digits=4,decimal_places=4)
    sector5 = models.DecimalField(max_digits=4,decimal_places=4)
    sector6 = models.DecimalField(max_digits=4,decimal_places=4)
    sector7 = models.DecimalField(max_digits=4,decimal_places=4)
    sector8 = models.DecimalField(max_digits=4,decimal_places=4)
    sector9 = models.DecimalField(max_digits=4,decimal_places=4)
    sector10 = models.DecimalField(max_digits=4,decimal_places=4)
    sector11 = models.DecimalField(max_digits=4,decimal_places=4)
    sector12 = models.DecimalField(max_digits=4,decimal_places=4)
    sector13 = models.DecimalField(max_digits=4,decimal_places=4)
    manager = models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Portfolio(models.Model):
    name = models.CharField(max_length=40)
    order = models.IntegerField()
    allocation = models.ForeignKey(Allocation,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    portfolio_value = models.DecimalField(max_digits=20,decimal_places=3)

class Holding(models.Model):
    ticker = models.CharField(max_length=9)
    quantity = models.DecimalField(max_digits=20,decimal_places=3)
    value = models.DecimalField(max_digits=20,decimal_places=3)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    asset_class = models.CharField(
        max_length = 60,
        choices = AssetClass.choices,
        default = AssetClass.EQUITIES,
    )
    sector = models.CharField(
        max_length = 60,
        choices = Sector.choices,
        default = Sector.OTHER,
    )
