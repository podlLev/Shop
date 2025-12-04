from django.http import HttpResponse
from .models import Category

def index(request):
    categories = Category.objects.all()
    output = '<h2>Список категорій та товарів</h2>'
    for i, category in enumerate(categories, start=1):
        output += f'<br>{i}. {category}<br>'
        for product in category.products.all():
            output += f'&nbsp;&nbsp;- {product}<br>'
    return HttpResponse(output)
