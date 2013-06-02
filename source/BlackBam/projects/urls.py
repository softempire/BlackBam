from django.conf.urls import patterns, include, url
from BlackBam.projects.views import index, ProjectList, ProjectDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/$', index),
    url(r'^api/project_list/$', ProjectList.as_view()),
)
