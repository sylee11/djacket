from django.urls import path

from .views import LatestProductList, DetailProduct, CategoryList, search

urlpatterns = [
    path('products/search', search),
    path('lastest-product', LatestProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', DetailProduct.as_view()),
    path('categories/<slug:category_slug>/', CategoryList.as_view()),
]