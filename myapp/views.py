from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . forms import CreateForm
from . models import Task

# Create your views here.

class index(CreateView):
    model = Task
    form_class = CreateForm
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context



class update(UpdateView):
    model = Task
    template_name = 'update.html'
    success_url = "/"



class delete(DeleteView):
    model = Task
    success_url = "/"
    template_name = 'delete.html'

