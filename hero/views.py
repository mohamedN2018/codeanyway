from django.shortcuts import render

# Create your views here.

app_name = 'hero'

def hero_view(request):
    
    return render(request, 'hero/hero.html')