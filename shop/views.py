from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Product

def index(request):
    return render(request, 'shop/index.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'categories'
    ordering = ['title']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Categories'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'
    ordering = ['-created_at']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'All Products'
        return context

    def get_queryset(self):
        return Product.objects.filter(is_active=True)

class ProductListByCategoryView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Product.objects.filter(category__slug=slug, is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['category'] = Category.objects.filter(slug=slug).first()
        context['page_title'] = context['category'].title if context['category'] else 'Products'
        return context