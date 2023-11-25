from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app_Jsonkeyvalueupdate import urls 


urlpatterns = [
    path('admin/', admin.site.urls),
]+ urls.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
