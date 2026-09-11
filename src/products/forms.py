from typing import ClassVar

from django import forms

from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields: ClassVar[list[str]] = ["title", "slug"]
        # fields = ['title', 'slug']
