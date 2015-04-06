from django.conf.urls import patterns, url

from salon import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^(?P<salon_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<salon_id>\d+)/(?P<service_id>\d+)/$', views.service, name='service'),	

)



