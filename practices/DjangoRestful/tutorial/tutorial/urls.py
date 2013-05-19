from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'tutorial.views.home', name='home'),
#    # url(r'^tutorial/', include('tutorial.foo.urls')),
#
#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#    url(r'^', include('snippets.urls')),
#)

urlpatterns = patterns(
    'snippets.views',
    url(r'^snippets/index', 'index'),
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)