from django.contrib import admin
from .models import Restaurant,ui_elements,booking,application_new_restaurant,info_text,message,support_message,\
request_token

@admin.register(Restaurant)
class adminRestaurant(admin.ModelAdmin):
    list_display = ['id', "owner_cafe",'Name_restaurant','rating','kitchen','average_check','photo_restaurant',
                    'photo_restaurant2','photo_restaurant3','menu_download','email',"phone","datetime"]
    list_filter = ["owner_cafe","rating","to_publish"]
@admin.register(ui_elements)
class adminui(admin.ModelAdmin):
    list_display = ['id','background','header',"ico_header"]



@admin.register(booking)
class admin_bookings(admin.ModelAdmin):
    list_display = ['id','restaurant','name','number',"places","date"]

@admin.register(application_new_restaurant)
class admin_application_new_restaurant(admin.ModelAdmin):
    list_display = ["id","user",'name_new_restaurant',"datetime","publish","blank","document1","document2","document3"]
    list_filter = ['id','name_new_restaurant',"user","publish","datetime"]


@admin.register(info_text)
class admin_info_text(admin.ModelAdmin):
    list_display = ["id","info_text_2"]


@admin.register(message)
class adminmessage(admin.ModelAdmin):
    list_display = ['id','message_user','heading','heading']
    list_filter = ["message_user"]

@admin.register(support_message)
class support_message_admin(admin.ModelAdmin):
    list_display = ['id',"application_user","message","datetime",'answered']
    list_filter = ["application_user"]
@admin.register(request_token)
class adminrequest_token(admin.ModelAdmin):
    list_display = ['id',"request_token_user","date_request"]
    list_filter = ['id',"request_token_user","date_request"]