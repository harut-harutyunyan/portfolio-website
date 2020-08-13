from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import *


@admin.register(PersonalInfo)
class AdminProject(admin.ModelAdmin):
    list_display = ('email', 'id')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('name', 'role')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


@admin.register(Job)
class AdminJob(admin.ModelAdmin):
    list_display = ('company', 'role')