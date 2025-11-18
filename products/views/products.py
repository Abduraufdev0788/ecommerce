from django.views import View
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404 
import json

from ..models import Category, Product, ProductImage



class ProductListView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = [
            {
                "id": product.pk,
                "name": product.name,
                "description": product.description,
                "price":float(product.price),
                "stock": product.stock,
                "is_active": product.is_active,
                "category": product.category.name,
                "category_id": product.category_id,
                "images": [
                    {
                        "id": img.id,
                        "url": img.image.url,
                        "alt_text": img.alt_text
                    }
                    for img in product.images.all()
                ],
                "created_at": product.created_at.isoformat(),
                "updated_at": product.updated_at.isoformat(),
                
            }
            for product in Product.objects.all()
        ]

        return JsonResponse({'products': products}, status = 201)

    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body)
        category = get_object_or_404(Category, pk=data['category_id'])

        name = data.get('name')
        if not name :
            return JsonResponse({"name": "Required"}, status = 400)
        elif len(name) > 256 :
            return JsonResponse({"name": "max 256 characters"}, status = 400)
        
        price = data.get("price")
        if not price:
            return JsonResponse({"price": "required"}, status = 400)
        elif len(str(price)) > 8:
            return JsonResponse({"price":"max 8 characters" }, status = 400)
        stock = data.get("stock")
        if not stock:
            return JsonResponse({"stock": "required"}, status = 400)   
        elif stock < 0 :
            return JsonResponse({"stock": "0 katta son kiriting"}, status = 400)
        
        try:
            Product.objects.get(name=name)
            return JsonResponse({'name': 'Unique.'}, status=400)
        except Product.DoesNotExist:
            product = Product(
                name = data['name'],
                description=data.get('description'),
                price = data.get('price'),
                stock = data.get('stock'),
                category = category,
                is_active = data.get('is_active')
            )
            product.save()

            return JsonResponse(
                {
                    "id": product.pk,
                    "name":product.name,
                    "description": product.description,
                    "price": product.price,
                    "stock":product.stock,
                    "is_active": product.is_active,
                    "category": category.name,
                    "category_id": category.id,
                    "created_at": product.created_at.isoformat(),
                    "updated_at": product.updated_at.isoformat()
                }, status = 201
            )
        
        


class ProductDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
