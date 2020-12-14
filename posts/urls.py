from django.urls import path

from django.conf.urls import  url
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	about,
	services,
	contact,
	)

app_name = 'posts'
urlpatterns = [

  path('',  post_list, name='list'),
  path('about/', about, name='about'),
  path('services/', services, name='services'),
  path('contact/', contact, name='contact'),
  path('create/', post_create),
  path('<slug:slug>/',post_detail, name='detail'),
  path('<slug:slug>/delete/', post_delete),
  path('<slug:slug>/edit/', post_update, name='update'),

]