from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from UniDjango.view import home
from contact.views import contactForm

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^contact/$', contactForm, name='contactForm'),
)
