from typing import ClassVar

from django import forms

from .models import Product

MY_CHOICES = [
    ("option1", "Option 1"),
    ("option2", "Option 2"),
    ("option3", "Option 3"),
]
YEARS = range(2000, 2031)  # Example range of years for the date field


class ProductModelForm(forms.ModelForm):
    labels: ClassVar[dict[str, str]] = {
        "title": "Product Title",
        "slug": "Product Slug",
        "price": "Product Price",
    }

    class Meta:
        model = Product
        fields = ("title", "slug", "price")
        # exclude = ("created_at", "updated_at")

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title and len(title) <= 10:
            raise forms.ValidationError(
                "Title must be at least 10 characters long."
            )
        return title

    def clean_slug(self):
        slug = self.cleaned_data.get("slug")
        if slug and len(slug) <= 10:
            raise forms.ValidationError(
                "Slug must be at least 10 characters long."
            )
        if "brand" not in slug:
            raise forms.ValidationError("Slug must contain the word 'brand'.")
        return slug

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price


class TestForm(forms.Form):
    date = forms.DateField(
        label="Date",
        required=False,
        widget=forms.SelectDateWidget(years=YEARS),
    )
    some_text = forms.CharField(
        label="some_text",
        widget=forms.Textarea(attrs={"rows": 4, "cols": 40}),
        max_length=100,
    )
    boolean = forms.BooleanField(label="Boolean", required=False)
    integer = forms.IntegerField(label="Integer", required=False)
    email = forms.EmailField(
        label="Email", required=False, initial="initial@example.com"
    )
    options = forms.CharField(
        label="Option",
        widget=forms.Select(choices=MY_CHOICES),
        required=False,
    )
    options_radio = forms.CharField(
        label="Option",
        widget=forms.RadioSelect(choices=MY_CHOICES),
        required=False,
    )
    options_checkbox = forms.CharField(
        label="Option",
        widget=forms.CheckboxSelectMultiple(choices=MY_CHOICES),
        required=False,
    )

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get("integer")
        if integer is not None and integer > 100:
            raise forms.ValidationError(
                "Integer must be a positive number less or equal to 100."
            )
        return integer

    def clean_some_text(self, *args, **kwargs):
        text = self.cleaned_data.get("some_text")
        if text and len(text) < 10:
            raise forms.ValidationError(
                "Text must be at least 10 characters long."
            )
        return text
