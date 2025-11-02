from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop_home'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<slug:slug>/', views.ProductListByCategoryView.as_view(), name='product_list_by_category'),
    path('categories/<slug:slug>/info/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<slug:slug>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/add/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
]
