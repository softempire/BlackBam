#coding=utf-8#

from django.contrib import admin
from BlackBam.projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'year')
    search_fields = ('name', 'address', 'year')
    list_filter = ('year',)
    ordering = ('year',)

admin.site.register(Project, ProjectAdmin)
