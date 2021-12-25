from django.shortcuts import render, redirect
from .models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    CHOICES = {'name': 'name', "min_price": 'price', "max_price": '-price' }
    sort = ''.join(request.GET.getlist('sort'))
    phones = Phone.objects.all()
    if sort != '':
        phones = Phone.objects.all().order_by(CHOICES[sort])
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)




def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
