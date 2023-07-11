from django.shortcuts import render
from .models import ContactMessage

# Create your views here.

def HOME(request):
    return render(request ,'home/home.html')

def SERVICE(request):
    return render(request ,'home/service.html')

def CONTACT(request):
    context = {}
    if request.method =='POST' :
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        print(data,title,email)
        
        if title =='' or email =='':
             context['status'] = 'Witaya'
             return render(request ,'home/contact.html',context)



        new =ContactMessage()
        new.title = title
        new.email = email
        new.detail = detail
        new.save()

        context['status'] = 'success'


    return render(request ,'home/contact.html',context)




