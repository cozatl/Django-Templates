from django.urls import path

from .views import ProductAPIView

urlpatterns = [
    # List all products or create a new product
    path("products/", ProductAPIView.as_view(), name="product-api"),
    # Query, update or delete a specific product by its ID
    path(
        "products/<int:pk>/",
        ProductAPIView.as_view(),
        name="product-detail",
    ),
]
