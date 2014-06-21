from __future__ import unicode_literals

from django.conf.urls import patterns, url

from rbpriority.extension import PriorityExtension


urlpatterns = patterns(
    'rbpriority.views',

    url(r'^$', 'configure'),
)