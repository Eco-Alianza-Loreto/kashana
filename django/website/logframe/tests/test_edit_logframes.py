# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from django_dynamic_fixture import N

from ..models import LogFrame
from ..views import EditLogframe


def test_redirects_to_logframe_management_page_on_success():
    edit_logframe_view = EditLogframe()
    logframe = N(LogFrame, persist_dependencies=False)
    edit_logframe_view.object = logframe
    assert reverse('logframe-dashboard', args=[logframe.organization.slug, logframe.slug]) == edit_logframe_view.get_success_url()
