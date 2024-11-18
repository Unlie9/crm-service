from django.urls import path
from payment.views import (
    PaymentCreateView,
    PaymentDeleteView,
    PaymentDetailView,
    PaymentListView,
    PaymentUpdateView
)


urlpatterns = [
    path("list/", PaymentListView.as_view(), name="payment-list"),
    path("detail/<int:pk>/", PaymentDetailView.as_view(), name="payment-detail"),
    path("create/", PaymentCreateView.as_view(), name="payment-create"),
    path("update/<int:pk>/", PaymentUpdateView.as_view(), name="payment-update"),
    path("delete/<int:pk>/", PaymentDeleteView.as_view(), name="payment-delete"),
]

app_name = "payment"
