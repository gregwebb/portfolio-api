from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
   path('my-nda', views.NDAView.as_view(), name="nda"),
]
