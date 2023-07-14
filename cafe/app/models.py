from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Restaurant(models.Model):
    Name_restaurant = models.CharField(max_length=15)
    Address = models.CharField(max_length=25)
    rating = models.IntegerField()
    about = models.TextField(max_length=400)
    terrace_restaurant = models.CharField(max_length=11)
    parking_restaurant = models.CharField(max_length=11)
    kitchen = models.CharField(max_length=20)
    average_check = models.IntegerField()
    photo_restaurant = models.ImageField(upload_to='photo_restaurant/')
    photo_restaurant2 = models.ImageField(upload_to='second_photo_restaurant/')
    photo_restaurant3 = models.ImageField(upload_to='third_photo_restaurant/')
    menu = models.ImageField(upload_to='menu_img/')
    menu_download = models.FileField(upload_to="media/menu/")
    email = models.EmailField()
    phone = PhoneNumberField(null=True)
    owner_cafe=models.OneToOneField("owner",on_delete=models.CASCADE,related_name="res",null=True)

    def __str__(self):
        return self.Name_restaurant



class ui_elements(models.Model):
    background=models.ImageField(upload_to='ui_bac_image/')
    header=models.ImageField(upload_to='ui_png/')
    ico_header=models.ImageField(upload_to='ico_header/')
    f_image = models.ImageField(upload_to='f_image/')
    complete_image=models.ImageField(upload_to="complete_image/",blank=True)

class booking(models.Model):
    restaurant = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    places = models.CharField(max_length=2)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class owner(models.Model):
    name_owner=models.CharField(max_length=15)
    last_name_owner=models.CharField(max_length=15)
    doc_1 = models.ImageField(upload_to='documents_owner/')
    doc_2 = models.ImageField(upload_to='documents_owner/')
    doc_3 = models.ImageField(upload_to='documents_owner/')

    def __str__(self):
        return self.name_owner


from django.db import models

# Create your models here.
