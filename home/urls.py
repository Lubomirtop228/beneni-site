
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name="home"),
    path('pepsi', views.pepsi_view, name="pepsi"),
]
