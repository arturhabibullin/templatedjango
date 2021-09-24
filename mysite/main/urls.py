from django.urls import path
from .views import *

urlpatterns = [
    path('', samples_list, name='samples_list_url'),
    path('sample/<str:sample>/', sample_detail, name='sample_detail_url'),
    path('companys/', companys_list, name='companys_list_url'),
    path('company/<str:slug>/', company_detail, name='company_detail_url'),
    path('categorys/', categorys_list, name='categorys_list_url'),
    path('category/<str:slug>/', category_detail,name='category_detail_url'),
    path('products/', products_list, name='pruducts_list_url'),
    path('product/<str:slug>/', product_detail, name='product_detail_url'),
    path('company-product/<str:company>/<str:product>/', company_product, name='company_product_url'),
    path('company-category/<str:company>/<str:category>/', company_category, name='company_category_url'),
    path('company-product-material/<str:company>/<str:product>/<str:material>/', company_product_material, name='company_product_material_url'),
    path('company-product-material-category/<str:company>/<str:product>/<str:material>/<str:category>/', company_product_material_category, name='company_product_material_category_url'),
]