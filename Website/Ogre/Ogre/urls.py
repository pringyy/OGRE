from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from points import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.user_login, name='index'),
    url(r'^points/', include('points.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'profile/', views.profile),
    url(r'^game_menu/$', views.game_menu, name = 'game_menu'),
    path('mytransaction/',views.pointlist,name='pointlist'),
    path('pointlist/',views.pointlist,name='pointlist'),
    path('pointcalculate/',views.pointcalculate,name = 'pointcalculate'),
    path('game1/',views.game1,name='game1'),
    path('game2/', views.game2, name = 'game2'),
    path('changeUsername/', views.changeUsername, name='changeUsername'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('changeAvatar/', views.changeAvatar, name = 'changeAvatar'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_DIR, document_root=settings.MEDIA_ROOT)