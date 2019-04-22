from django.db import models


from django.contrib.auth.models import User


class internprofile(models.Model):      #model for creating new intern records

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
