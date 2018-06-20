from django.conf.urls import url
from django.contrib import admin
from shippings.views import get_name
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', get_name),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)