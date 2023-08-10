from django.contrib import admin
from .models import Restaurant,ui_elements,booking,application_new_restaurant,info_text
@admin.register(Restaurant)
class adminRestaurant(admin.ModelAdmin):
    list_display = ['id', "owner_cafe",'Name_restaurant','rating','kitchen','average_check','photo_restaurant',
                    'photo_restaurant2','photo_restaurant3','menu_download','email',"phone"]
    list_filter = ["owner_cafe","rating","to_publish"]
@admin.register(ui_elements)
class adminui(admin.ModelAdmin):
    list_display = ['id','background','header',"ico_header"]



@admin.register(booking)
class admin_bookings(admin.ModelAdmin):
    list_display = ['id','restaurant','name','number',"places","date"]

@admin.register(application_new_restaurant)
class admin_application_new_restaurant(admin.ModelAdmin):
    list_display = ["id",'name_new_restaurant']
    list_filter = ['id','name_new_restaurant']


@admin.register(info_text)
class admin_info_text(admin.ModelAdmin):
    list_display = ["id","info_text_2"]