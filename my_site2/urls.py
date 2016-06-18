from django.conf.urls import patterns, include, url
from django.contrib import admin
from restaurant.views import menu

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_site2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',menu),
    url(r'^admin/', include(admin.site.urls)),
)
