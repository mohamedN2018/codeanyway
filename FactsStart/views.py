from django.shortcuts import render
from FactsStart.models import factsStart
from contact.models import info, social_media_info
from hero.models import Hero, HeroSlider
# Create your views here.


def FactsStart(request):
    facts = factsStart.objects.all()
    # contact models
    info_contact = info.objects.first()
    social_media_contacts = social_media_info.objects.all()

    # hero models
    hero_sliders = HeroSlider.objects.first()
    heroes = Hero.objects.all()

    context = {
        'info_contact': info_contact,
        'social_media_contacts': social_media_contacts,
        'hero_sliders': hero_sliders,
        'heroes': heroes,
        'facts': facts,
    }
    return render(request, 'facts.html', context)
