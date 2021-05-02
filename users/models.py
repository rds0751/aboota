from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.utils.html import mark_safe


class User(AbstractUser, PermissionsMixin):
    name = models.CharField(_("User's name"), blank=True, max_length=255)
    picture = models.ImageField(
        _("Profile picture"), upload_to="profile_pics/", null=True, blank=True
    )
    location = models.CharField(_("Location"), max_length=50, null=True, blank=True)
    job_title = models.CharField(_("Job title"), max_length=50, null=True, blank=True)
    personal_url = models.URLField(
        _("Personal URL"), max_length=555, blank=True, null=True
    )
    facebook_account = models.URLField(
        _("Facebook profile"), max_length=255, blank=True, null=True
    )
    twitter_account = models.URLField(
        _("Twitter account"), max_length=255, blank=True, null=True
    )
    github_account = models.URLField(
        _("GitHub profile"), max_length=255, blank=True, null=True
    )
    linkedin_account = models.URLField(
        _("LinkedIn profile"), max_length=255, blank=True, null=True
    )
    short_bio = models.CharField(
        _("Describe yourself"), max_length=60, blank=True, null=True
    )
    bio = models.CharField(_("Short bio"), max_length=280, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, unique=True)
    mobile = models.CharField(max_length=255)
    referal = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, default=False)
    friends = models.ManyToManyField("User", related_name='user_friends', blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile", "username"]
    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_profile_name(self):
        if self.name:
            return self.name

        return self.username