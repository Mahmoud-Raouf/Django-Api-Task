from django.shortcuts import render ,get_object_or_404
from django.contrib.auth.models import User
from .models import Product



def product_list(request):
    product_list = Product.objects.all()
    context = {
        'product_list' : product_list
    }
    return render(request, 'product/product_list.html', context)


##Show one note
def product_details(request, slug):
    product_detail = Product.objects.get(PROSlug=slug)
    context= {
        'product_detail' : product_detail
    }
    return render(request, 'product/product_detail.html', context)
