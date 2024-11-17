from django.shortcuts import render
from django.views import generic



class SiteListView(generic.ListView):
    ...

class SiteDetailView(generic.DetailView):
    ...

class SiteCreateView(generic.CreateView):
    ...


class SiteUpdateView(generic.UpdateView):
    ...


class SiteDeleteView(generic.DeleteView):
    ...