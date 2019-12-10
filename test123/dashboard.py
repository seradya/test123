"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'test123.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration" & "Applications"
        self.children.append(modules.Group(
            _('Администрирование'),
            column=1,
            collapsible=True,
            children = [
                modules.AppList(
                    _('Круто'),
                    column=1,
                    collapsible=False,
                    models=('django.contrib.*',),
                ),
                modules.AppList(
                    _('Пользователи'),
                    column=1,
                    collapsible=False,
                    models=('auth123.models.CustomUser',),
                )
            ]
        ))

        self.children.append(modules.Group(
            _('Магазин'),
            column=2,
            collapsible=True,
            children=[
                modules.AppList(
                    _('Клиенты'),
                    column=2,
                    collapsible=True,
                    models=('main.models.Client',),
                ),
                modules.AppList(
                    _('Товары'),
                    column=2,
                    collapsible=True,
                    models=('main.models.Service',),
                ),
            ]
        ))


        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Последние действия'),
            limit=5,
            collapsible=True,
            column=3,
        ))
