from django.shortcuts import render
from .models import Infos
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail


def contact(request):
    infos = Infos.objects.first()
    if request.method == 'POST':
        subject = request.POST['Subject']
        email_from = request.POST['email']
        message = request.POST['message']
        recipient = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, email_from, recipient)
    return render(request, 'contact/contact.html', {'infos': infos})
