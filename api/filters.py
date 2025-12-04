import django_filters

from shop.models import Product, Category


class CategoryFilter(django_filters.FilterSet):
    created_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    has_active_products = django_filters.BooleanFilter(method='filter_active_products')

    class Meta:
        model = Category
        fields = ['title']

    def filter_active_products(self, queryset, name, value):
        if value:
            return queryset.filter(products__is_active=True).distinct()
        return queryset


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_qty = django_filters.NumberFilter(field_name="product_qty", lookup_expr='gte')
    max_qty = django_filters.NumberFilter(field_name="product_qty", lookup_expr='lte')
    created_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'is_active']
