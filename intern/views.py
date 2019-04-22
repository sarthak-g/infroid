from django.shortcuts import redirect,render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import internprofile
# Create your views here.

class InternView(ListView): #view for list of all interns
    model = internprofile
    template_name = 'internList.html'
    context_object_name = 'internlist'
class InternCreateView(CreateView): #view for create new intern(done only by internAdmin not by superuser)
    model = internprofile
    template_name = 'profile_create.html'
    fields = '__all__'
    success_url = reverse_lazy('intern_list')
class InternUpdateView(UpdateView): #view for updating specific details of intern(done only by internAdmin not by superuser)
    model = internprofile
    template_name = 'profile_edit.html'
    fields = ['full_name','email','stipend','date_of_joining','date_of_leaving','internship_admin_remark','internship_status']
    success_url = reverse_lazy('intern_list')
class InternDeleteView(DeleteView): #view for deleting particular intern record(done only by internAdmin not by superuser)
    model = internprofile
    template_name = 'profile_delete.html'
    context_object_name = 'delTODO'
    success_url = reverse_lazy('intern_list')

def ActiveIntern(request): #view for filtering interns having status as Active
    active = internprofile.objects.filter(internship_status='Active')
    return render(request,"active.html",{'active':active})

def ParticularRecordView(request): #view for interns to see their profile
    record = internprofile.objects.get(email=request.user.email)
    return render(request,"particular_record.html",{'record':record})
class ParticularUpdateView(UpdateView):  #view for interns to edit their some specific details 
    model = internprofile
    template_name = 'particular_edit.html'
    fields = ['phone_number','profile_picture','document_file']
    success_url = reverse_lazy('particular_record')
