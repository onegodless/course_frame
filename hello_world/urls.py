from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.hello_world_view, name='hello_world'),
]
