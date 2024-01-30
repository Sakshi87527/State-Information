from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import state
from .forms import stateform
from django.urls import reverse_lazy

# Create your views here.

class form(CreateView):
    model = state
    form_class = stateform
    template_name = "stateform.html"
    success_url = reverse_lazy('show')
class show(ListView):
    model = state
    template_name = "statelist.html"
    context_object_name = "stateobj"

class update(UpdateView):
    model=state
    template_name="update.html"
    form_class=stateform
    success_url=reverse_lazy("show")               

class delete(DeleteView):
    model=state
    template_name="confirm_delete.html"
    success_url=reverse_lazy("show")