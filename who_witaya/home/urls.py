from django.urls import path
from .views import HOME,SERVICE
from .views import HOME

urlpatterns = [
    path('', HOME),
    path('service/', SERVICE),



]