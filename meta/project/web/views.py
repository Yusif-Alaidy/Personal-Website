from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Frontend(request):
    return render(request, 'front-end.html')

def Backend(request):
    return render(request, 'back-end.html')

def Contact(request):
    if request == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contact Form',#title
            message, #message
            'settings.EMAIL_HOST_USER',
            ['nourenaalaidy@gmail.com'],
            fail_silently=False)
    return render(request, 'contact.html', )

def Portfolio(request):
    return render(request, 'portfolio.html')