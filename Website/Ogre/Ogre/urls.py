from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from points import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.user_login, name='index'),
    url(r'^points/', include('points.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
     path('mytranscation/',views.pointlist,name='pointlist'),
    path('ajaxpointlist/',views.ajaxpointlist,name='ajaxpointlist'),
    path('game/',views.game,name='game'),
    path('changenickname/', views.changenickname, name='changenickname')
    
]