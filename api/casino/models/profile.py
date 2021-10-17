from django.db import models
from django.conf import settings

class Profile(models.Model):
    # company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendor_company')
    company_name = models.CharField(default='', max_length=200)