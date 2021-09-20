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
    


]