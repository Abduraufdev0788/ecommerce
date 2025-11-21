import json

from django.views import View
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404

from ..models import Order, OrderItem


class OrderStatusView(View):

    def patch(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
