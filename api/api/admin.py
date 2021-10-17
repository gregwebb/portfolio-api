from django.contrib import admin

from api.models import Portfolio,User,Allocation,Holding

admin.site.register(Portfolio)
admin.site.register(User)
admin.site.register(Allocation)
admin.site.register(Holding)
