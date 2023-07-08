from django.urls import path
from .views import HOME

urlpatterns = [
    path('', HOME),
]