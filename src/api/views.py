from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from ecommerce.models import ProductModel

from .serializers import ProductSerializer


class ProductAPIView(views.APIView):
    # GET: List all or query by ID/slug (if passed via query params or kwargs)
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            product = get_object_or_404(ProductModel, pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)

        products = ProductModel.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST: Create a new product
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT: Update a product completely by its ID (pk)
    def put(self, request, pk=None, *args, **kwargs):
        product = get_object_or_404(ProductModel, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH: Partial update of a product
    def patch(self, request, pk=None, *args, **kwargs):
        product = get_object_or_404(ProductModel, pk=pk)
        serializer = ProductSerializer(
            product, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Delete a product
    def delete(self, request, pk=None, *args, **kwargs):
        product = get_object_or_404(ProductModel, pk=pk)
        product.delete()
        return Response(
            {"message": f"Product with ID {pk} deleted successfully."},
            status=status.HTTP_200_OK,
        )
