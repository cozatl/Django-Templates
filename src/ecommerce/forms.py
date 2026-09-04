from django import forms

from .models import ProductModel


# Starting form model
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [  # noqa: RUF012
            "title",
            "description",
            "price",
            "seller",
            "color",
            "product_dimensions",
        ]