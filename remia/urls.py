from django.conf.urls import url
from django.contrib import admin
from shippings.views import get_name

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', get_name),
]