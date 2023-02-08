"""Clear Django Cache app."""
from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem

from .views import clear_cache


@hooks.register("register_settings_menu_item")
def register_cache_menu_item():
    """Register a new menu item URL."""
    return MenuItem(
        "Clear Cache",
        reverse("wagtailadmin_clear_cache"),
        classnames="icon icon-folder-open-inverse",
        order=999,
    )


@hooks.register("register_admin_urls")
def urlconf_clear_cache():
    """Register a new admin url."""
    return [path("clear-cache/", clear_cache, name="wagtailadmin_clear_cache")]
