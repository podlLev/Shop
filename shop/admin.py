from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at',)
    list_display_links = ('title',)
    search_fields = ('title', 'slug', 'created_at',)
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ('title', 'created_at',)
    list_editable = ('slug',)
    ordering = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'product_qty', 'category_link', 'slug', 'is_active', 'created_at',)
    list_display_links = ('title',)
    search_fields = ('title', 'category__title', 'price', 'slug', 'product_qty',)
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ('title', 'is_active', 'created_at',)
    list_editable = ('price', 'product_qty', 'slug', 'is_active',)
    ordering = ('-created_at',)

    @admin.display(description='Category')
    def category_link(self, obj):
        url = reverse('admin:shop_category_change', args=[obj.category.id])
        return mark_safe(f'<a href="{url}">{obj.category.title}</a>')
