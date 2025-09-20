from django.shortcuts import render

# Create your views here.

def features_start(request):
    
    return render(request, 'FeaturesStart/features_start.html')
