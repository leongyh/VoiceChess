from django.conf.urls import patterns, url

from Chess import views

urlpatterns = patterns('',
	url(r'^test$', views.recieveCommand, name='recieveCommand'),
	url(r'^testing$', views.testing, name='test'),
	url(r'^getmove$', views.getMove, name='getMove'),	
)
