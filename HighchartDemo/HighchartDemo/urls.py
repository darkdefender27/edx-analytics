from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'hdapp.views.main'),

    url(r'^index/$', 'hdapp.views.index'),
    url(r'^stats1/$', 'hdapp.views.stats_one'),
    url(r'^stats2/$', 'hdapp.views.stats_two'),
    url(r'^stats3/$', 'hdapp.views.stats_three'),
    url(r'^stats4/$', 'hdapp.views.stats_four'),
)
