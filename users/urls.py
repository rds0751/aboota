from django.conf.urls import url

from . import views
from binary import views as binary_views

app_name = "users"
urlpatterns = [
    url(regex=r"^$", view=views.UserDashboardView.as_view(), name="list"),
    url(regex=r"^~redirect/$", view=views.UserRedirectView.as_view(), name="redirect"),
    url(regex=r"^~update/$", view=views.UserUpdateView.as_view(), name="update"),
    url(regex=r"^profile/$", view=views.profile.as_view(), name="profile"),
    url(regex=r"^change-password/$", view=views.changepassword.as_view(), name=""),
    url(regex=r"^(?P<username>[\w.@+-]+)/$", view=views.UserDetailView.as_view(), name="detail"),
]