from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class internprofile(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to="profile_img",height_field=None, width_field=None, max_length=100)
    document_file = models.FileField(upload_to="document_img",max_length=100)
    stipend = models.CharField(max_length=10)
    date_of_joining = models.DateField(auto_now=False, auto_now_add=False)
    date_of_leaving = models.DateField(auto_now=False, auto_now_add=False)
    internship_admin_remark = models.TextField()

    OPTION_CHOICES = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
    )
    internship_status = models.CharField(choices=OPTION_CHOICES, max_length=128)
    
