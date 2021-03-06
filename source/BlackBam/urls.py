from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'projects/', include('BlackBam.projects.urls')),
    url(r'labors/', include('BlackBam.labors.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
)
