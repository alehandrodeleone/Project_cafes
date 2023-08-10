from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Restaurant(models.Model):
    Name_restaurant = models.CharField(max_length=15)
    Address = models.CharField(max_length=25)
    rating = models.IntegerField(null=True)
    about = models.TextField(max_length=400)
    terrace_restaurant = models.CharField(max_length=11)
    parking_restaurant = models.CharField(max_length=11)
    kitchen = models.CharField(max_length=20)
    average_check = models.IntegerField()
    photo_restaurant = models.ImageField(upload_to='photo_restaurant/')
    photo_restaurant2 = models.ImageField(upload_to='second_photo_restaurant/')
    photo_restaurant3 = models.ImageField(upload_to='third_photo_restaurant/')
    menu_download = models.FileField(upload_to="menu/")
    email = models.EmailField()
    phone = PhoneNumberField(null=True)
    owner_cafe=models.OneToOneField(User,on_delete=models.CASCADE,related_name="res",null=True)
    to_publish=models.BooleanField(default=False)


    def __str__(self):
        return self.Name_restaurant



class ui_elements(models.Model):
    background=models.ImageField(upload_to='ui_bac_image/')
    header=models.ImageField(upload_to='ui_png/')
    ico_header=models.ImageField(upload_to='ico_header/')
    ico_setting_header = models.ImageField(upload_to='ico_header/',null=True)
    f_image = models.ImageField(upload_to='f_image/')
    complete_image=models.ImageField(upload_to="complete_image/",blank=True)
    new_restaurant_setting_img=models.ImageField(upload_to="setting_img/",blank=True)
    edit_restaurant_setting_img = models.ImageField(upload_to="setting_img/", blank=True)
    user_setting_img = models.ImageField(upload_to="setting_img/", blank=True)
    support_setting_img=models.ImageField(upload_to="setting_img/", blank=True)

class booking(models.Model):
    restaurant = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    places = models.CharField(max_length=2)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class application_new_restaurant(models.Model):
    name_new_restaurant=models.CharField(max_length=15)
    blank = models.FileField(upload_to="documents_owner/")
    document1 = models.FileField(upload_to="documents_owner/")
    document2 = models.FileField(upload_to="documents_owner/")
    document3 = models.FileField(upload_to="documents_owner/")

class info_text(models.Model):
    info_text_1 = models.TextField(max_length=800, null=True)
    info_text_2 = models.CharField(max_length=25, null=True)



