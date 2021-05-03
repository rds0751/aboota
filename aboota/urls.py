from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('meeting/', include('meeting.urls')),
    path('accounts/', include('allauth.urls')),
    path('budget/',include('budget.urls')),
    path('todo/', include("todo.urls", namespace="todo")),
]