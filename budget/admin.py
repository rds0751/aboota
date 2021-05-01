from django.contrib import admin

# Register your models here.
from .models import ExpenseInfo

admin.site.register(ExpenseInfo)