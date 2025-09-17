from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    # Django urls لتغيير اللغة
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='core'),
    path('contact/', include('contact.urls'), name='contact'),
    path('blog/', include('blog.urls'), name='blog'),
    path('hero/', include('hero.urls'), name='hero'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
