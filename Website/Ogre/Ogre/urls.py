from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from points import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.user_login, name='index'),
    url(r'^points/', include('points.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$',views.profile,name='profile'),
     path('mytranscation/',views.pointlist,name='pointlist'),
    path('ajaxpointlist/',views.ajaxpointlist,name='ajaxpointlist'),
    path('game/',views.game,name='game'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)