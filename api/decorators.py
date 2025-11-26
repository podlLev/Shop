from functools import wraps

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


def cache_page_per_object(timeout, key_prefix=""):
    def decorator(func):
        @wraps(func)
        def wrapper(view, request, *args, **kwargs):
            slug = kwargs.get('slug', '')
            full_key_prefix = f"{key_prefix}_{slug}" if key_prefix else slug
            decorated_func = method_decorator(cache_page(timeout, key_prefix=full_key_prefix))(func)
            return decorated_func(view, request, *args, **kwargs)
        return wrapper
    return decorator
