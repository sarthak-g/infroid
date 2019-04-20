from django.shortcuts import redirect,render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import internprofile
# Create your views here.

class InternView(ListView):
    model = internprofile
    template_name = 'internList.html'
    context_object_name = 'internlist'
class InternCreateView(CreateView):
    model = internprofile
    template_name = 'profile_create.html'
    fields = '__all__'
    success_url = reverse_lazy('intern_list')
class InternUpdateView(UpdateView):
    model = internprofile
    template_name = 'profile_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('intern_list')
class InternDeleteView(DeleteView):
    model = internprofile
    template_name = 'profile_delete.html'
    context_object_name = 'delTODO'
    success_url = reverse_lazy('intern_list')
