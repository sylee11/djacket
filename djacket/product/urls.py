from django.urls import path, include

from .views import LatestProductList, DetailProduct

urlpatterns = [
    path('lastest-product', LatestProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', DetailProduct.as_view()),
]