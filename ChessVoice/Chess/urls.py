from django.conf.urls import patterns, url

from Chess import views

urlpatterns = patterns('',
	url(r'^test$', views.recieveCommand, name='recieveCommand'),
)