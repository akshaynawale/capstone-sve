from django.conf.urls import url

from . import views

urlpatterns = [ url(r'^$', views.index, name='index'),
		url(r'^images/$', views.ShowImages, name='images'),
		url(r'^instances/$', views.ShowInstances, name='instances'),
		url(r'^interfaces/$', views.ShowInterfaces, name='interfaces'),
		url(r'^StartInstance/$', views.StartInstance, name="StartInstance"),] 
		
