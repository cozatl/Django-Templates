from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from .forms import ProductModelForm
from .models import ProductModel

# Create your views here.

def product_model_delete_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Product deleted successfully")
        return HttpResponseRedirect('/ecommerce/')
    context = { "product": instance }
    template = "ecommerce/delete-view.html"
    return render(request, template, context)

def product_model_update_view(request, product_id= None):
    instance = get_object_or_404(ProductModel, id=product_id)
    form = ProductModelForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Product updated successfully")
        return HttpResponseRedirect('/ecommerce/{product_id}/'.format(product_id=instance.id))
    context = { "form": form }
    template = "ecommerce/update-view.html"
    return render(request, template, context)

def product_model_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Product created successfully")
        return HttpResponseRedirect('/ecommerce/{product_id}/'.format(product_id=instance.id))
    context = { "form": form }
    template = "ecommerce/create-view.html"
    return render(request, template, context)

def product_model_detail_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    context = { "product": instance }
    template = "ecommerce/detail-view.html"
    return render(request, template, context)

#@login_required(login_url='/admin/login/')   # This decorator ensures that only authenticated users can access this view. If a user is not logged in, they will be redirected to the login page.
# @login_required                               # Defined in settings.py as LOGIN_URL = "/admin/login/"
def product_model_list_view(request):
    print('user:',request.user)
    query = request.GET.get('q', None)
    queryset = ProductModel.objects.all()

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    template = "ecommerce/list-view.html"
    context = { "products": queryset }

    if request.user.is_authenticated:
        template = "ecommerce/list-view.html"
    else:
        template = "ecommerce/list-view-public.html"

    return render(request, template, context)

@login_required                               # Defined in settings.py as LOGIN_URL = "/admin/login/"
def login_required_view(request):
    print('user:',request.user)
    queryset = ProductModel.objects.all()
    template = "ecommerce/list-view.html"
    context = { "products": queryset }

    if request.user.is_authenticated:
        template = "ecommerce/list-view.html"
    else:
        template = "ecommerce/list-view-public.html"

    return render(request, template, context)