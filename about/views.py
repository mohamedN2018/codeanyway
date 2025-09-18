from django.shortcuts import render
from contact.models import info, social_media_info
from hero.models import Hero, HeroSlider

# Create your views here.

def AboutPageView(request):


    # contact models
    info_contact = info.objects.first()
    social_media_contacts = social_media_info.objects.all()

    # hero models
    hero_sliders = HeroSlider.objects.first()
    heroes = Hero.objects.all()


    context ={
        'info_contact': info_contact,
        'social_media_contacts': social_media_contacts,
        'hero_sliders': hero_sliders,
        'heroes': heroes,
    }
    return render(request, 'about/about.html', context)