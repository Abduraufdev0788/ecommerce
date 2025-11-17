from django.views import View
from django.http import JsonResponse, HttpRequest

from ..models import Category, Product, ProductImage


class ProductSearchView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass
