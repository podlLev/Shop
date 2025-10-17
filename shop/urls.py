from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop_home'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/', views.ProductListByCategoryView.as_view(), name='product_list_by_category'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
]
