from django.urls import path

from .views import (
    OrderListView,
    OrderDetailView,
    OrderStatusView,
    OrderPaymentStatusView,
)


urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/status/', OrderStatusView.as_view(), name='order-status'),
    path('orders/<int:pk>/payment-status/', OrderPaymentStatusView.as_view(), name='order-payment-status'),
]
