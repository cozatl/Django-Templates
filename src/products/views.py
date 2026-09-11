from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
)

from .forms import ProductModelForm
from .mixins import TemplateTitleMixin
from .models import DigitalProduct, Product


class ProtectedProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductModelForm
    template_name = "products/product_detail.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return self.object.get_edit_url()


class ProtectedProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "forms_delete.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return "/products/products"


class ProtectedProductCreateView(
    LoginRequiredMixin, TemplateTitleMixin, CreateView
):
    model = Product
    template_name = "forms.html" # REVIEW
    title = "Create Product"
    fields = ('title', 'slug')

    def form_valid(self, form):
        # Set the user of the product to the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProductIDRedirectView(RedirectView):
    """
    Redirects from a product's slug URL to its ID-based URL.
    """

    # permanent = True  # Use a permanent redirect (HTTP 301)

    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        pk = url_params.get("pk")       
        # Get the product based on the slug from the URL
        # product = get_object_or_404(Product, slug=kwargs['slug'])
        product = get_object_or_404(Product, pk=pk)
        slug = product.slug
        print("testy",slug)
        # Redirect to the product's detail page using its ID
        return f"/products/products/{slug}/"


class ProductRedirectView(RedirectView):
    """
    Redirects from a product's slug URL to its ID-based URL.
    """

    # permanent = True  # Use a permanent redirect (HTTP 301)

    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        slug = url_params.get("slug")
        print("test",slug)
        # Redirect to the product's detail page using its ID
        return f"/products/products/{slug}/"


class DigitalProductListView(TemplateTitleMixin, ListView):
    model = DigitalProduct
    template_name = "products/product_list.html"
    title = "Digital Products"


class ProtectedProductListView(LoginRequiredMixin, ListView):
    model = DigitalProduct
    template_name = "products/product_list.html"
    title = "Protected Products"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class ProductListView(TemplateTitleMixin, ListView):
    # app_label = "products"
    # model = Product
    # view_name = list
    # template_name = <app_name>/<model>_<view_name>.html
    model = Product
    template_name = "products/product_list.html"
    title = "Physical Products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProtectedProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"
