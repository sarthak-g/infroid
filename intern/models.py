from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# class User(AbstractUser):
#     is_intern = models.BooleanField(default=True)

# Create your models here.

class internprofile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name="person", null=True, blank=True)
    username = models.CharField(max_length=30,default='')
    password = models.CharField(max_length=30,default='')
    full_name = models.CharField(max_length=30,blank=False)
    email = models.EmailField(max_length=254,blank=False)
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to="profile_img",height_field=None, width_field=None, max_length=100)
    document_file = models.FileField(upload_to="document_img",max_length=100)
    stipend = models.CharField(max_length=10,blank=False)
    date_of_joining = models.DateField(auto_now=False, auto_now_add=False,null=False,blank=False)
    date_of_leaving = models.DateField(auto_now=False, auto_now_add=False,null=False,blank=False)
    internship_admin_remark = models.TextField()
    class Meta:
        verbose_name = 'Internprofile'
        verbose_name_plural = 'Internprofiles'


    OPTION_CHOICES = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
    )
    internship_status = models.CharField(choices=OPTION_CHOICES, max_length=128)
