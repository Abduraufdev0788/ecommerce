from django.views import View
from django.http import JsonResponse, HttpRequest
from django.db.models import Q

from ..models import Category, Product, ProductImage


class ProductSearchView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        params = request.GET
        products = Product.objects.all()

        search = params.get('search')
        if search:
            products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))

        category = params.get("category")
        if category:
            products = products.filter(category__id=category)

        is_active = params.get("is_active")
        if is_active:
            if is_active == 'true':
                products = products.filter(is_active=True)
            elif is_active == 'false':
                products = products.filter(is_active=False)

        min_price = params.get("min_price")
        if min_price:
            products = products.filter(price__gte=min_price)

        max_price = params.get("max_price")
        if max_price:
            products = products.filter(price__lte=max_price)

        in_stock = params.get("in_stock")
        if in_stock:
            if in_stock == 'true':
                products = products.filter(stock__gt=0)
            elif in_stock == 'false':
                products = products.filter(stock=0)

        result = []
        for p in products:
            result.append({
                "id": p.pk,
                "name": p.name,
                "description": p.description,
                "price": p.price,
                "stock": p.stock,
                "is_active": p.is_active,
                "category": p.category.name if p.category else None,
                "category_id": p.category_id,
                "images": [
                    {
                        "id": img.pk,
                        "url": img.image.url,
                        "alt_text": img.alt_text
                    }
                    for img in p.images.all()
                ],
                "created_at": p.created_at.isoformat(),
                "updated_at": p.updated_at.isoformat(),
            })

        return JsonResponse({"products": result, "result": len(result)})