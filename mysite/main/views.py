from .models import *
from django.shortcuts import render

# Create your views here.
def companys_list(request):
    companys = Company.objects.all()
    context = {
        'companys':companys,
    }
    return render(request, 'main/companys_list.html', context)

def company_detail(request, slug):
    company = Company.objects.get(slug=slug)
    samples = company.sample_set.all()
    product = Product.objects.filter(sample__company__slug=slug).distinct()
    context = {
        'company':company,
        'samples':samples,
        'product':product
       
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
    companys = Company.objects.all()
    context = {
        'samples':samples,
        'companys':companys,
    }
    return render(request, 'main/samples_list.html', context)

def sample_detail(request, sample):
    sample = Sample.objects.get(sample=sample)
    company = sample.company
    product = sample.product
  
    context = {
        'sample':sample,
        'company':company,
        'product':product,
        
    }
    return render(request, 'main/sample_detail.html', context)

def company_product(request,company, product):
    company = Company.objects.get(slug=company)
    product = Product.objects.get(slug=product)
    samples = Sample.objects.filter(company=company,product=product)
    comp_slug = company.slug
    pro_slug = product.slug
    category = Category.objects.filter(samples__company__slug=comp_slug, samples__product__slug=pro_slug).distinct()
    materials = Material.objects.filter(sample__company__slug=comp_slug, sample__product__slug=product.slug).distinct()
    context = {
       'samples':samples,
       'category':category,
       'company':company,
       'materials':materials,
       'product':product,
    }
    return render(request, 'main/company_product.html', context)

def company_category(request, company, category):
    company = Company.objects.get(slug=company)
    category = Category.objects.get(slug=category)
    samples = Sample.objects.filter(company=company, categorys=category)
    context = {
        'samples':samples,
        'company':company,
    }
    return render(request, 'main/company_category.html', context)

def company_product_material(request, company, product, material):
    company = Company.objects.get(slug=company)
    product = Product.objects.get(slug=product)
    material = Material.objects.get(slug=material)
    samples = Sample.objects.filter(company=company, product=product, material=material)
    company_obj = company.slug
    product_obj = product.slug
    material_obj = material.slug
    categorys = Category.objects.filter(samples__company__slug=company_obj, samples__product__slug=product_obj, samples__material__slug=material_obj).distinct()
    context = {
        'company':company,
        'product':product,
        'material':material,
        'samples':samples,
        'categorys':categorys,


    }
    return render(request, 'main/company_product_material.html', context)

def company_product_material_category(request, company, product, material, category):
    company = Company.objects.get(slug=company)
    product = Product.objects.get(slug=product)
    material = Material.objects.get(slug=material)
    category = Category.objects.get(slug=category)
    company_obj = company.slug
    product_obj = product.slug
    material_obj = material.slug
    category_obj = category.slug
    samples = Sample.objects.filter(company=company, product=product, material=material, categorys=category)
    context = {
        'samples':samples,
    }
    return render(request, 'main/company_product_material_category.html', context)