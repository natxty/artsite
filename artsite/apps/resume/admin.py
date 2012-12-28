from django.contrib import admin
from models import Resume
from django.contrib.admin import TabularInline, StackedInline
from django.conf import settings


admin.site.register(Resume)