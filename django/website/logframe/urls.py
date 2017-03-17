from django.conf.urls import include, url
from .views import (
    CreateLogframe, DeleteLogframe, EditLogframe, ResultEditor, ResultMonitor
)

logframe_management_patterns = [
    url(r'^(?P<org_slug>[\w\d_-]+)/create/', CreateLogframe.as_view(), name='create-logframe'),
    url(r'^update/(?P<slug>[\w\d_-]+)/$', EditLogframe.as_view(), name='update-logframe'),
    url(r'^delete/(?P<slug>[\w\d_-]+)/$', DeleteLogframe.as_view(), name='delete-logframe'),
]

urlpatterns = [
    url(r'^design/(?P<logframe_id>\d+)/result/(?P<pk>\d+)/$',
        ResultEditor.as_view(),
        name="design-result"),
    url(r'^monitor/(?P<logframe_id>\d+)/result/(?P<pk>\d+)/$',
        ResultMonitor.as_view(),
        name="monitor-result"),
    url('^logframes/', include(logframe_management_patterns))
]
