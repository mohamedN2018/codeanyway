from . views import FactsStart
from django.urls import path

app_name = 'FactsStart'

urlpatterns = [
    path('', FactsStart.as_view(), name='facts_start'),
]
