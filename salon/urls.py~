from django.conf.urls import patterns, url

from salon import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<salon_id>\d+)/$', views.detail, name='detail'),
)



