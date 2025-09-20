from django.shortcuts import render
# app
from contact.models import info, social_media_info
from hero.models import Hero, HeroSlider
from FactsStart.models import factsStart
from about.models import About, DetailsSmall, About_Ar, DetailsSmall_Ar
from FeaturesStart.models import FeatureStart, FeatureItem
from services.models import ServiceStart, ServiceItem
# Create your views here.

def home(request):
    # contact models
    info_contact = info.objects.first()
    social_media_contacts = social_media_info.objects.all()

    # hero models
    hero_sliders = HeroSlider.objects.first()
    heroes = Hero.objects.all()

    # facts start model
    facts = factsStart.objects.all()

    # about 
    Abouts = About.objects.first()
    DetailsSmalls = DetailsSmall.objects.all()
    # about ar
    Abouts_ar = About_Ar.objects.first()
    DetailsSmalls_ar = DetailsSmall_Ar.objects.all()

    # features start
    FeaturesStarts = FeatureStart.objects.first()
    FeatureItems = FeatureItem.objects.all()

    # serve the context to the template
    service_starts = ServiceStart.objects.first()
    service_items = ServiceItem.objects.all()[:5]
 

    context = {
        'info_contact': info_contact,
        'social_media_contacts': social_media_contacts,
        'hero_sliders': hero_sliders,
        'heroes': heroes,
        'facts': facts,
        'Abouts': Abouts,
        'DetailsSmalls': DetailsSmalls,
        'Abouts_ar': Abouts_ar,
        'DetailsSmalls_ar': DetailsSmalls_ar,
        'FeaturesStarts': FeaturesStarts,
        'FeatureItems': FeatureItems,
        'service_starts': service_starts,
        'service_items': service_items,
    }
    return render(request, 'home.html', context)