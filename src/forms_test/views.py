from django.forms import modelformset_factory
from django.shortcuts import render

from .forms import ProductModelForm
from .models import Product

# def home(request):
#     initial_data = {
#         "some_text": "Initial text",
#         "boolean": True,
#         "integer": 42,
#         # 'email': 'initial@example.com'
#     }
#     form = TestForm(request.POST or None, initial=initial_data)
#     if form.is_valid():
#         # Process the form data here
#         print(form.cleaned_data)
#     return render(request, "forms.html", {"form": form})

# def home(request):
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ProductModelForm()
#     return render(request, "forms.html", {"form": form})

# def home(request):
#     # 'extra' defines how many empty forms will be displayed in the formset
#     TestFormSet = formset_factory(TestForm, extra=3)
#     formset = TestFormSet(request.POST or None)
#     for form in formset:
#         print(form.data)
#     context = {"formset": formset}
#         # if form.is_valid():
#         #     form.save()
#     return render(request, "formset_view.html", context)


def home(request):
    ProductModelFormSet = modelformset_factory(Product, form=ProductModelForm)
    formset = ProductModelFormSet(
        request.POST or None, queryset=Product.objects.all()
    )

    print(
        "Formset data:", formset.data
    )  # Debugging line to print formset data

    print(
        "Formset errors:", formset.errors
    )  # Debugging line to print formset errors

    formset.clean()  # Call the clean method to trigger validation
    if formset.is_valid():
        print("Formset is valid. Saving data...")
        formset.save()

    context = {"formset": formset}
    return render(request, "formset_view.html", context)
