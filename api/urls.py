from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='categories-list-create'),
    path('categories/<slug:slug>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductListCreateView.as_view(), name='products-list'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]
