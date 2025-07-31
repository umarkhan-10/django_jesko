from django.contrib import admin
from django.urls import path,include
from . import veiws
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', veiws.index, name='index'),
    path('home', veiws.home, name='home'),
    path('about', veiws.about, name='about'),
    #Contact apps url
    path('contact/', include('contact.urls')),
    path('games/', include('games.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)