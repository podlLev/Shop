from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from api.decorators import cache_page_per_object
from api.filters import ProductFilter, CategoryFilter
from api.permissions import IsAdminOrAuthenticatedReadOnly
from api.serializers import CategorySerializer, ProductSerializer
from shop.models import Category, Product


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CategoryFilter
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'created_at']
    ordering = ['title']

    @method_decorator(cache_page(60 * 15, key_prefix='category_list'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    lookup_field = 'slug'

    @cache_page_per_object(60 * 15, key_prefix='category_detail')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'product_qty', 'created_at']
    ordering = ['-created_at']

    @method_decorator(cache_page(60 * 15, key_prefix='product_list'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    lookup_field = 'slug'

    @cache_page_per_object(60 * 15, key_prefix='product_detail')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
