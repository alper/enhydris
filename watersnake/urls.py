from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'watersnake.views.index', name='index'),
)
