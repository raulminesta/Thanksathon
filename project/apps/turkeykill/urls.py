from django.conf.urls import patterns, url
from apps.turkeykill import views
urlpatterns = patterns('',
	# url(r'^process/$', views.process, name="process"),
	# url(r'^update/(?P<product_id>\d+)/$', views.update, name="update"),
	# url(r'^delete/(?P<product_id>\d+)/$', views.delete, name="delete"),
	# url(r'^create/$', views.create, name= 'create'),
	# url(r'^show/(?P<product_id>\d+)/$', views.show, name="show"),
	url(r'^reset/$', views.reset),
	url(r'^attack/$', views.attack_turkey, name="attack"),
	url(r'^$', views.index, name='index'),
)