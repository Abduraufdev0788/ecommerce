from django.views import View
from django.http import JsonResponse, HttpRequest

from ..models import Category, Product, ProductImage



class ProductListView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass

    def post(self, request: HttpRequest) -> JsonResponse:
        pass


class ProductDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass

    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
