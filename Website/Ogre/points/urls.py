
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^ogre_points/$', views.ogre_points, name = 'ogre_points'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^getmypoint/$',views.getmypoint,name='getmypoint'),
]