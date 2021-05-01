from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('app/',views.index,name='index'),
    path('add_item/',views.add_item,name='add item'),
]