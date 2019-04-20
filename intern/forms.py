# from django.contrib.auth.models import User
# from .models import internprofile
# from django import forms
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
# class InternProfileForm(forms.ModelForm):
#     class Meta:
#         model = internprofile
#         fields = ('full_name','email','phone_number','profile_picture','document_file','stipend','date_of_joining','date_of_leaving','internship_admin_remark','internship_status')

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User
# from .models import internprofile,CustomUser
class RegisterInternForm(UserCreationForm):
    # declare the fields you will show
    username = forms.CharField(label="Your Username")
    # first password field
    password1 = forms.CharField(label="Your Password",widget=forms.PasswordInput)
    # confirm password field
    password2 = forms.CharField(label="Repeat Your Password",widget=forms.PasswordInput)


    full_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    phone_number = forms.CharField(max_length=10)
    # profile_picture = forms.ImageField(upload_to="profile_img",height_field=None, width_field=None, max_length=100)
    # document_file = forms.FileField(upload_to="document_img",max_length=100)
    stipend = forms.CharField(max_length=10)
    date_of_joining = forms.DateField()
    date_of_leaving = forms.DateField()
    internship_admin_remark = forms.CharField(widget=forms.Textarea)

    OPTION_CHOICES = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
    )
    internship_status = forms.CharField()



    # this sets the order of the fields
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password1", "password2", 'full_name','email','phone_number',)
