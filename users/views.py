from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import requests
from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpRequest, Http404
from django.template import RequestContext
from django.conf import settings
from django.shortcuts import reverse
from payu.utils import generate_hash, verify_hash
from django.contrib.auth.decorators import login_required 

from django.contrib.auth import get_user_model
User = get_user_model()

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

class SearchListView(ListView):
    model = User
    template_name = "/users/password_reset_done.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get("query")
        context["hide_search"] = True
        context["user"] = (
            get_user_model()
            .objects.get(Q(username__iexact=query) | Q(mobile__iexact=query))
        )
        
        return context

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name", "email", "mobile", "address", "city", "state",
    ]
    model = User
    
    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:update")

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserDashboardView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/user_dashboard.html'
    def get_context_data(self, *args, **kwargs):
        self.request.session['user_id'] = self.request.user.username
        context = super().get_context_data(*args, **kwargs)
        return context

class profile(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/profile.html'
    slug_field = "username"
    slug_url_kwarg = "username"

def validate_username(request):
    username = request.GET.get('username', None)
    print(username)
    try:
        u = User.objects.get(username=username).name
    except Exception as e:
        u = 'Sorry Username Does not Exists or {}'.format(e)
    data = {
        'is_taken': u
    }
    return JsonResponse(data)