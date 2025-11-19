from django.views import View
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404

from ..models import Product, ProductImage


class ProductImageListView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        images = [
            {
                "id": image.pk,
                "url": f"{request.build_absolute_uri()}{image.image.url}",
                "alt_text": image.alt_text,
                "product_id": image.product.pk,
                "product_name": image.product.name,
                "created_at": image.created_at.isoformat()
            }
            for image in ProductImage.objects.all()
        ]
        return JsonResponse({'images': images})

    def post(self, request: HttpRequest) -> JsonResponse:
        data = request.POST

        product_id = data.get('product_id')
        if not product_id:
            return JsonResponse([{'product_id': 'Required.'}], status=400)
        
        image = request.FILES.get('image')
        if not image:
            return JsonResponse([{'image': 'Required.'}], status=400)
        
        product = get_object_or_404(Product, pk=product_id)
        new_image = ProductImage(
            image=image,
            product=product,
            alt_text=data.get('alt_text')
        )
        new_image.save()

        return JsonResponse(
            {
                "id": new_image.pk,
                "url": f"{request.build_absolute_uri()}{new_image.image.url}",
                "alt_text": new_image.alt_text,
                "product_id": new_image.product.pk,
                "product_name": new_image.product.name,
                "created_at": new_image.created_at.isoformat()
            },
            status=201
        )


class ProductImageDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        image = get_object_or_404(ProductImage, pk=pk)

        return JsonResponse(
            {
                "id": image.pk,
                "url": f"{request.build_absolute_uri()}{image.image.url}",
                "alt_text": image.alt_text,
                "product_id": image.product.pk,
                "product_name": image.product.name,
                "created_at": image.created_at.isoformat()
            },
            status=201
        )

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        image = get_object_or_404(ProductImage, pk=pk)

        data = request.POST

        image.alt_text = data.get('alt_text', image.alt_text)

        return JsonResponse(
            {
                "id": image.pk,
                "url": f"{request.build_absolute_uri()}{image.image.url}",
                "alt_text": image.alt_text,
                "product_id": image.product.pk,
                "product_name": image.product.name,
                "created_at": image.created_at.isoformat()
            },
            status=204
        )

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        impage = get_object_or_404(ProductImage, pk=pk)

        impage.delete()

        return JsonResponse({'image': 'Deleted.'}, status=204)
