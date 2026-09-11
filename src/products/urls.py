from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView, TemplateView

from products.views import (
    DigitalProductListView,
    ProductDetailView,
    ProductIDRedirectView,
    ProductListView,
    ProductRedirectView,
    ProtectedProductCreateView,
    ProtectedProductDeleteView,
    ProtectedProductListView,
    ProtectedProductUpdateView,
    # ProtectedProductDetailView,
)

# Create your views here.
urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
        name="admin",
    ),
    path(
        "about/",
        TemplateView.as_view(template_name="about.html"),
        name="about",
    ),
    path(
        "about-us/",
        RedirectView.as_view(url="/products/about/"),
        name="about-us",
    ),
    path(
        "team/",
        TemplateView.as_view(template_name="team.html"),
        name="team",
    ),
    path(
        "products/",
        ProductListView.as_view(),
        name="product-list",
    ),
    path(
        "digital-products/",
        DigitalProductListView.as_view(),
        name="digital-product-list",
    ),
    path(
        "my-products/",
        ProtectedProductListView.as_view(),
        name="digital-product-list",
    ),
    path(
        "products/<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
    path(
        "products/<slug:slug>/",
        ProductDetailView.as_view(),
        name="product-detail",
    ),
    path(
        "p/<int:pk>/",
        ProductIDRedirectView.as_view(),
        name="product-detail",
    ),
    path(
        "p/<slug:slug>/",
        ProductRedirectView.as_view(),
        name="product-detail",
    ),
    # path(
    #     "my-products/<slug:slug>/",
    #     ProtectedProductDetailView.as_view(),
    #     name="product-detail",
    # ),
    path(
        "my-products/create/",
        ProtectedProductCreateView.as_view(),
        name="product-create",
    ),
    path(
        "my-products/<slug:slug>/",
        ProtectedProductUpdateView.as_view(),
        name="product-detail",
    ),
    path(
        "my-products/<slug:slug>/delete/",
        ProtectedProductDeleteView.as_view(),
        name="product-detail",
    ),
]
