from django.conf.urls import patterns, include, url
from payments import views
from django.contrib import admin
admin.autodiscover()
from django.conf import settings


# This is Django1.5
#ipdb.set_trace()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'main.views.index'),
    url(r'^$', include('main.urls')),
    url(r'^hello$', 'url_test.views.index', name='hello'),
    # ('^pages/', include('django.contrib.flatpages.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    # user registration/authentication
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'^register$', views.register, name='register'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^circle_item', 'main.views.circle_item', name='circle_item'),
  #  url(r'^report$',' main.views.report', name='report'),
)
'''
# This is Django1.8
urlpatterns = ['',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.index'),
#    url(r'^$', include('main.urls')),
    url(r'^hello$', 'url_test.views.index', name='hello'),
    # ('^pages/', include('django.contrib.flatpages.urls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    # user registration/authentication
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_out$', views.sign_out, name='sign_out'),
    url(r'^register$', views.register, name='register'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^circle_item', 'main.views.circle_item', name='circle_item'),
    # This line cause a very strange problem and take me lots time on debug it
    #url(r'^report$',' main.views.report', name='report'),
    ]
'''

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),]
