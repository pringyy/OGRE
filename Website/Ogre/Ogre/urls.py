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
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.profile),
    url(r'^game_menu/$', views.game_menu, name = 'game_menu'),
    path('mytransaction/',views.pointlist,name='pointlist'),
    path('ajaxpointlist/',views.ajaxpointlist,name='ajaxpointlist'),
    path('pointcalculate/',views.pointcalculate,name = 'pointcalculate'),
    path('game1/',views.game1,name='game1'),
    path('game2/', views.game2, name = 'game2'),
    url(r'^iterateJSON/$', views.iterateJSON, name='iterateJSON'),
    path('changeUsername/', views.changeUsername, name='changeUsername'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)