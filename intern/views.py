from django.shortcuts import redirect,render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import internprofile
from .forms import RegisterInternForm
# from .forms import UserForm,InternProfileForm
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
    fields = ['full_name','email','stipend','date_of_joining','date_of_leaving','internship_admin_remark','internship_status']
    success_url = reverse_lazy('intern_list')
class InternDeleteView(DeleteView):
    model = internprofile
    template_name = 'profile_delete.html'
    context_object_name = 'delTODO'
    success_url = reverse_lazy('intern_list')

def ActiveIntern(request):
    active = internprofile.objects.filter(internship_status='Active')
    return render(request,"active.html",{'active':active})

def CreateView(request):
    if request.method == 'POST':
        form = RegisterInternForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect("intern_list")
    else:
        form = RegisterInternForm()
    return render(request, 'profile_create.html', { 'form': form })
def ParticularRecordView(request):
    record = internprofile.objects.all()
    return render(request,"particular_record.html",{'record':record})
class ParticularUpdateView(UpdateView):
    model = internprofile
    template_name = 'particular_edit.html'
    fields = ['phone_number','profile_picture','document_file']
    success_url = reverse_lazy('particular_record')
# def intern_profile_view(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, prefix='UF')
#         profile_form = InternProfileForm(request.POST, prefix='PF')
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save(commit=False)
#             user.save()
#             user.intern_profile.full_name = profile_form.cleaned_data.get('full_name')
#             user.intern_profile.email = profile_form.cleaned_data.get('email')
#             user.intern_profile.phone_number = profile_form.cleaned_data.get('phone_number')
#             user.intern_profile.profile_picture = profile_form.cleaned_data.get('profile_picture')
#             user.intern_profile.document_file = profile_form.cleaned_data.get('document_file')
#             user.intern_profile.stipend = profile_form.cleaned_data.get('stipend')
#             user.intern_profile.date_of_joining = profile_form.cleaned_data.get('date_of_joining')
#             user.intern_profile.date_of_leaving = profile_form.cleaned_data.get('date_of_leaving')
#             user.intern_profile.internship_admin_remark = profile_form.cleaned_data.get('internship_admin_remark')
#             user.intern_profile.internship_status = profile_form.cleaned_data.get('internship_status')
#             user.intern_profile.save()
#     else:
#         user_form = UserForm(prefix='UF')
#         profile_form = InternProfileForm(prefix='PF')
#     return render(request, 'profile_create.html',{
# 			'user_form': user_form,
# 			'profile_form': profile_form,
#             })
