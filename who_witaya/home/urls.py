from django.urls import path
from .views import *


urlpatterns = [
    path('', HOME ,name= 'homepage'),
    path('service/', SERVICE ,name= 'service'),
    path('contact/', CONTACT ,name= 'contact'),



]