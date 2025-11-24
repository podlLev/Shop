from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

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


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    lookup_field = 'slug'


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'product_qty', 'created_at']
    ordering = ['-created_at']


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    lookup_field = 'slug'
