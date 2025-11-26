from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_redis import get_redis_connection
from rest_framework.authtoken.models import Token

from shop.models import Product, Category


redis = get_redis_connection("default")

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver([post_save, post_delete], sender=Category)
def invalidate_category_cache(sender, instance, **kwargs):
    for key in redis.scan_iter("*category_list*"):
        redis.delete(key)
    for key in redis.scan_iter(f"*category_detail*{instance.slug}*"):
        redis.delete(key)

@receiver([post_save, post_delete], sender=Product)
def invalidate_product_cache(sender, instance, **kwargs):
    for key in redis.scan_iter("*product_list*"):
        redis.delete(key)
    for key in redis.scan_iter(f"*product_detail*{instance.slug}*"):
        redis.delete(key)
