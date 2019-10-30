from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^points/', include('points.urls')),
    url(r'^admin/', admin.site.urls),
]