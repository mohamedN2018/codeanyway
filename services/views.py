from django.shortcuts import render
from services.models import ServiceStart, ServiceItem

from contact.models import info, social_media_info
from hero.models import Hero, HeroSlider

# Create your views here.

def services(request):
    # contact models
    info_contact = info.objects.first()
    social_media_contacts = social_media_info.objects.all()

    # hero models
    hero_sliders = HeroSlider.objects.first()
    heroes = Hero.objects.all()

    service_starts = ServiceStart.objects.first()
    service_items = ServiceItem.objects.all()


    context = {
        # Add any context variables if needed
        'service_starts': service_starts,
        'service_items': service_items,
        'info_contact': info_contact,
        'social_media_contacts': social_media_contacts,
        'hero_sliders': hero_sliders,
        'heroes': heroes,
    }
    return render(request, 'home_services/services_list.html', context)
    

def service_detail(request, slug):
    service_item = ServiceItem.objects.filter(slug=slug).first()

    # contact models
    info_contact = info.objects.first()
    social_media_contacts = social_media_info.objects.all()

    # hero models
    hero_sliders = HeroSlider.objects.first()
    heroes = Hero.objects.all()

    context = {
        'service_item': service_item,
        'info_contact': info_contact,
        'social_media_contacts': social_media_contacts,
        'hero_sliders': hero_sliders,
        'heroes': heroes,
    }
    return render(request, 'home_services/service_detail.html', context)