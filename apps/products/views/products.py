import json

from django.views import View
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404

from ..models import Product, Category


class ProductListView(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        products = [p.to_dict() for p in Product.objects.all()]

        return JsonResponse({"products": products})


    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body)

        name = data.get("name")
        if not name:
            return JsonResponse({"name": "Required."}, status=400)
        if len(name) > 256:
            return JsonResponse({"name": "Max 256 characters."}, status=400)

        if data.get("price") is None:
            return JsonResponse({"price": "Required."}, status=400)

        stock = data.get("stock")
        if stock is None:
            return JsonResponse({"stock": "Required."}, status=400)
        if stock < 0:
            return JsonResponse({"stock": "Must be positive."}, status=400)

        category = None
        category_id = data.get("category_id")
        if category_id:
            category = get_object_or_404(Category, pk=category_id)

        product = Product.objects.create(
            name=data["name"],
            description=data.get("description"),
            price=data["price"],
            stock=data["stock"],
            category=category,
            is_active=data.get("is_active", True)
        )

        return JsonResponse(product.to_dict(), status=201)


class ProductDetailView(View):

    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        product = get_object_or_404(Product, pk=pk)

        return JsonResponse(product.to_dict())


    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        product = get_object_or_404(Product, pk=pk)
        data = json.loads(request.body)

        category_id = data.get('category_id')
        category = None
        if category_id:
            category = get_object_or_404(Category, pk=category_id)

        product = get_object_or_404(Product, pk=pk)

        data = json.loads(request.body) if request.body else {}

        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.category = category if category is not None else product.category
        product.is_active = data.get('is_active', product.is_active)

        product.save()

        return JsonResponse(product.to_dict(), status=204)
    
    def delete(self, request: HttpRequest, pk:int) -> JsonResponse:
        product = get_object_or_404(Product, pk=pk)

        product.delete()

        return JsonResponse({'product': 'Deleted.'}, status=204)
    
