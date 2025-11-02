from django.db.models import Min, Max, Avg
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import ProductForm, CategoryForm
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


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'shop/form.html'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'category'
        context['action'] = 'Add'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/form.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'product'
        context['action'] = 'Add'
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.object.products.filter(is_active=True)

        context['min_price'] = products.aggregate(Min('price'))['price__min']
        context['max_price'] = products.aggregate(Max('price'))['price__max']
        context['avg_price'] = products.aggregate(Avg('price'))['price__avg']
        context['avg_qty'] = products.aggregate(Avg('product_qty'))['product_qty__avg']
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'shop/form.html'
    context_object_name = 'category'

    def get_success_url(self):
        return reverse_lazy('category_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'category'
        context['action'] = 'Update'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/form.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'product'
        context['action'] = 'Update'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'shop/form_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'category'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/form_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'product'
        return context
