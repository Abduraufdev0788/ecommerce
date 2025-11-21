import json

from django.views import View
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404

from ..models import Order, OrderItem


class OrderListView(View):

    def get(self, request: HttpRequest) -> JsonResponse:
        pass


    def post(self, request: HttpRequest) -> JsonResponse:
        pass


class OrderDetailView(View):

    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk:int) -> JsonResponse:
        pass
