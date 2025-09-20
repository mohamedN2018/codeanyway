from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.services, name='services'),
    path('<slug:slug>/', views.service_detail, name='service_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)