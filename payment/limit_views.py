from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views import generic

from payment.models import Limit
from payment.forms import PaymentForm


class LimitListView(generic.ListView):
    model = Limit
    template_name = "limit/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Limits"] = Limit.objects.all()
        
        return context
    

class LimitCreateView(generic.CreateView):
    model = Limit
    template_name = "limit/form.html"
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
                "message": "Limit success",
                "redirect_url": reverse_lazy("payment:payment-list")
            }, status=200)
        
        return super().form_valid(form)

class PaymentUpdateView(LimitCreateView, generic.UpdateView):
    pass


class LimitDeleteView(generic.DeleteView):
    model = Limit
    template_name = "limit/delete.html"
    success_url = reverse_lazy("payment:payment-list")
