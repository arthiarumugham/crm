""" Lists all the urls relevant to Tickets App """
from django.conf.urls import url
from . import views

urlpatterns = [
	   url(r'^list/$', views.show_tickets, name='show_tickets')
]
