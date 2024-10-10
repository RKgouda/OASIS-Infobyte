from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import TODO
# Register your models here.
admin.site.register(TODO)