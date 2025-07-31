from django.contrib import admin
from django.urls import path,include
from . import veiws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', veiws.index, name='index'),
    path('home', veiws.home, name='home'),
    path('about', veiws.about, name='about'),
    #Contact apps url
    path('contact/', include('contact.urls')),
]
