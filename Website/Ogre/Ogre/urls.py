from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from points import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^points/', include('points.urls')),
    url(r'^admin/', admin.site.urls),
]