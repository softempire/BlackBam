from django.conf.urls import patterns, include, url
from BlackBam.projects import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/$', views.ProjectList.as_view()),
)
