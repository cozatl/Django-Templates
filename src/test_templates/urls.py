from django.contrib import admin
from django.urls import path

from .views import test_view

# Create your views here.
urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
        name="admin",
    ),
    path(
        "",
        test_view,
        name="test_view",
    ),
]
