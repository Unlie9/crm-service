from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views import generic

from payment.models import Payment
from payment.forms import PaymentForm


def index(request):
    context = {
        'title': 'Index Page',
        'message': 'Welcome to the Index Page without a model!',
    }
    return render(request, "index.html", context)


class PaymentListView(generic.ListView):
    model = Payment
    template_name = "payment/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["payments"] = Payment.objects.all()
        
        return context


class PaymentDetailView(generic.DetailView):
    model = Payment
    template_name = "payment/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["payment"] = self.object
        
        return context


class PaymentCreateView(generic.CreateView):
    model = Payment
    template_name = "payment/form.html"
    form_class = PaymentForm
    success_url = reverse_lazy("payment:payment-list")

    def form_invalid(self, form):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "success": False,
                "errors": form.errors,
              }, status=400)
        
        return super().form_invalid(form)
    
    def form_valid(self, form):
        self.object = form.save()
        
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "success": True,
                "message": "Payment success",
                "redirect_url": reverse_lazy("payment:payment-list")
            }, status=200)
        
        return super().form_valid(form)

class PaymentUpdateView(PaymentCreateView, generic.UpdateView):
    pass


class PaymentDeleteView(generic.DeleteView):
    model = Payment
    template_name = "payment/delete.html"
    success_url = reverse_lazy("payment:payment-list")


class CreateLimitView(generic.CreateView):
    ...
