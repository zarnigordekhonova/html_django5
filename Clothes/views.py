from django.shortcuts import render
from .models import types, wears

# Create your views here.
def get_info(request):
    type = types.objects.all()
    context = {
        'type': type
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    products = wears.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)