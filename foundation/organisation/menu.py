from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from .models import Project, Theme, NetworkGroup


class ProjectMenu(CMSAttachMenu):

    name = _("Projects")

    def get_nodes(self, request):
        nodes = []
        for project in Project.objects.all():
            node = NavigationNode(
                project.name,
                project.get_absolute_url(),
                project.pk,
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(ProjectMenu)


class ThemeMenu(CMSAttachMenu):

    name = _("Themes")

    def get_nodes(self, request):
        nodes = []
        for theme in Theme.objects.all():
            node = NavigationNode(
                theme.name,
                theme.get_absolute_url(),
                theme.pk,
                )
            nodes.append(node)
        return nodes

menu_pool.register_menu(ThemeMenu)


class NetworkGroupMenu(CMSAttachMenu):

    name = _('Network Group')

    def get_nodes(self, request):
        nodes = []
        for group in NetworkGroup.objects.countries():
            node = NavigationNode(
                group.get_country_display(),
                group.get_absolute_url(),
                group.pk,
            )
            nodes.append(node)

            for regiongroup in NetworkGroup.objects\
                    .regions(country=group.country_slug):
                node = NavigationNode(
                    regiongroup.region,
                    regiongroup.get_absolute_url(),
                    regiongroup.pk,
                    group.pk,
                    )
                nodes.append(node)
        return nodes

menu_pool.register_menu(NetworkGroupMenu)
