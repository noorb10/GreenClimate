from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include 

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projectWeb.urls')), #include is function that helps in including url paths from url file of app (projectWeb.urls) inside of the main project website urls (climateChange.urls)
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 