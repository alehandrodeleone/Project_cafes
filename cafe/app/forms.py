from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Restaurant

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class save_applicationForm(forms.ModelForm):
#     class Meta:
#         model=application_new_restaurant
#         fields= ['name_new_restaurant', 'blank', 'document1', 'document2', 'document3']

class edit_restaurantForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields=["Name_restaurant","Address","about","terrace_restaurant","parking_restaurant","average_check","photo_restaurant",
                "photo_restaurant2","photo_restaurant3","menu_download","email","phone"]
        



