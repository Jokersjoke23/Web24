from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CategoryListView,
    CategoryDetailView,
    CategoryProductsView,
)

urlpatterns = [
    path("api/products/", ProductListView.as_view(), name="product-list"),
    path("api/products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("api/categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "api/categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"
    ),
    path(
        "api/categories/<int:id>/products/",
        CategoryProductsView.as_view(),
        name="category-products",
    ),
]
