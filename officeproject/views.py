from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import RegisterForm
def home(request):
    # user = get_user_model()

    # u =User.objects.values()


    users = User.objects.filter(is_superuser=False)

    return render(request,"home.html",{'users':users})
def index(request):
    return render(request,"index.html")



def SignUpView(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, 'signup.html', { 'form': form })


def delete_user(request, username):
    context = {}

    try:
        u = User.objects.get(username=username)
        u.delete()
        msg = 'The user is deleted.'
    except User.DoesNotExist:
        msg = 'User does not exist.'
    except Exception as e:
        msg = e.message

    return render(request, 'delete_user.html',{'msg':msg})
class update_user(UpdateView):
    model = User
    template_name = 'update_user.html'
    fields = ['username','first_name','last_name','email',]
    success_url = reverse_lazy('home')
