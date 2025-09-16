from django.shortcuts import render
from .models import info, social_media_info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

app_name = 'contact'

def contact_home(request):
    info_contact = info.objects.first()
    social_media_contacts = social_media_info.objects.all()


    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        
    context = {
        'info_contact': info_contact,
        'social_media_contacts': social_media_contacts,
    }
    return render(request, 'contact_home.html', context)



