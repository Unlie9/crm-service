from django.shortcuts import render
from django.views import generic



class InvoiceListView(generic.ListView):
    ...

class InvoiceDetailView(generic.DetailView):
    ...

class InvoiceCreateView(generic.CreateView):
    ...


class InvoiceUpdateView(generic.UpdateView):
    ...


class InvoiceDeleteView(generic.DeleteView):
    ...


class InvoiceCloneView(generic.CreateView):
    ...
