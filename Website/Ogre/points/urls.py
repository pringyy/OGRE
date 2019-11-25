
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^ogre_points/$', views.ogre_points, name = 'ogre_points')
]