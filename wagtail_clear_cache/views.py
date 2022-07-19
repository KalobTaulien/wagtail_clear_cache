"""Clear tempalte caching."""
from django.contrib import messages
from django.core.cache import cache
from django.shortcuts import redirect
from django.urls import reverse


def clear_cache(request):
    """Simple function to clear template caching."""
    cache.clear()
    messages.success(request, "Template cache cleared.")
    return redirect(reverse("wagtailadmin_home"))
