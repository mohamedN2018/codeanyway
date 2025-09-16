from django.shortcuts import render

# Create your views here.

def contact_home(request):
    return render(request, 'contact_home.html')