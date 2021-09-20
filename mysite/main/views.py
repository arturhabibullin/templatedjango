from main.models import Category, Company, Product, Sample
from django.shortcuts import render

# Create your views here.
def companys_list(request):
    companys = Company.objects.all()
    context = {
        'companys':companys
    }
    return render(request, 'main/companys_list.html', context)

def company_detail(request, slug):
    company = Company.objects.get(slug=slug)
    sample=company.sample_set.all()

    context = {
        'company':company,
        'sample':sample,
    }
    return render(request, 'main/company_detail.html', context)

def categorys_list(request):
    categorys = Category.objects.all()
    context = {
        'categorys':categorys
    }
    return render(request, 'main/categorys_list.html', context)


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'category':category
    }
    return render(request, 'main/category_detail.html', context)

def products_list(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'main/products_list.html', context)

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    sample=product.sample_set.all()
    context = {
        'product':product,
        'sample':sample
    }
    return render(request, 'main/product_detail.html', context)

def samples_list(request):
    samples = Sample.objects.all()
    context = {
        'samples':samples
    }
    return render(request, 'main/samples_list.html', context)

def sample_detail(request, sample):
    sample = Sample.objects.get(sample=sample)
    company = sample.company
    product = sample.product
    context = {
        'sample':sample,
        'company':company,
        'product':product
    }
    return render(request, 'main/sample_detail.html', context)