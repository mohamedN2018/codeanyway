from django.shortcuts import render

from contact.models import info, social_media_info

# Create your views here.

def home(request):
    info_contact = info.objects.first()
    social_media_contacts = social_media_info.objects.all()
    
    context = {
        'info_contact': info_contact,
        'social_media_contacts': social_media_contacts,
    }
    return render(request, 'home.html', context)