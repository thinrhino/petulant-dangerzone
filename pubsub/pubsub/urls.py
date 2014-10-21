from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'api.views.home', name='home'),
    url(r'^send-message/$', 'api.views.send_message', name='send_message'),

)
