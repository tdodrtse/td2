from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        (r'^polls/$', 'mysite.polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'mysite.polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'mysite.polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'mysite.polls.views.vote'),
    (r'^admin/', include(admin.site.urls)),

)
