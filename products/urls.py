from django.urls import path

from .views import (
    CategoryListView,
    CategoryDetailView,
    ProductListView,
    ProductDetailView,
    ProductImageListView,
    ProductImageDetailView,
    ProductSearchView,
)


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('images/', ProductImageListView.as_view(), name='image-list'),
    path('images/<int:pk>/', ProductImageDetailView.as_view(), name='image-detail'),
]
