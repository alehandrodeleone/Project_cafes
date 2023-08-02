from django.contrib import admin
from .models import Restaurant,ui_elements,booking
@admin.register(Restaurant)
class adminRestaurant(admin.ModelAdmin):
    list_display = ['id', "owner_cafe",'Name_restaurant','rating','kitchen','average_check','photo_restaurant',
                    'photo_restaurant2','photo_restaurant3','menu','menu_download','email',"phone"]
@admin.register(ui_elements)
class adminui(admin.ModelAdmin):
    list_display = ['id','background','header',"ico_header"]



@admin.register(booking)
class admin_bookings(admin.ModelAdmin):
    list_display = ['id','restaurant','name','number',"places","date"]
    #
    # restaurants = models.CharField(max_length=20)
    # name = models.CharField(max_length=20)
    # number = models.CharField(max_length=20)
    # places = models.CharField(max_length=2)
    # date = models.DateTimeField(auto_now_add=True)


from django.contrib import admin

# Register your models here.
