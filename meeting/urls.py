from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('',views.index,name='index'),
    url(r"join/", views.join, name="join"),
]