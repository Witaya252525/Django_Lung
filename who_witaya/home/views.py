from django.shortcuts import render

# Create your views here.

def HOME(request):
    return render(request ,'home/home.html')

def SERVICE(request):
    return render(request ,'home/service.html')

def CONTACT(request):
    return render(request ,'home/contact.html')



