from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^sms/$', 'phonely.views.sms'),
	url(r'^$','phonely.views.index'),
)
