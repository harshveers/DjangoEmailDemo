from django.conf.urls import url

from . import views

urlpatterns = [
    # Auth API
    url(r'^$', views.index, name='index'),
	url(r'^send_email$', views.send_email, name='send_email'),
]