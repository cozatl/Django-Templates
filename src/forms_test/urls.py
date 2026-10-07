from django.contrib import admin
from django.urls import path

from .views import home

# Create your views here.
urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
        name="admin",
    ),
    path(
        "",
        home,
        name="home",
    ),
]
