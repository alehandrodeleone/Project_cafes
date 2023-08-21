
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings
from app.views import*
from rest_framework.routers import DefaultRouter#### Необходим для маршрутизации Viewsets drf
from app.views import start_page,save_data,\
    register,login_view,\
    user_page,setting_user,\
    application_new_res,save_application,\
    edit_restaurant,complete_html,profile_and_mail,\
    support,save_request_token,\
    api_page,api_page_2,UserCreateView,RESTAURANT,Search_RESTAURANT,work_with_restaurant


router = DefaultRouter()
router.register(r'work_with_restaurant', work_with_restaurant)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',start_page,name="start_page"),
    path('complete/', save_data, name='save_data'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path("user_page/",user_page,name="user_page"),
    path("setting_user/",setting_user,name="setting_user"),
    path("application_new_res",application_new_res,name='application_new_res'),
    path('save_application/', save_application, name='save_application_send'),
    path('edit_restaurant/',edit_restaurant, name="edit_restaurant"),
    path("complete_page/",complete_html,name="complete_page"),
    path("profile/",profile_and_mail, name="profile"),
    path("support/",support,name="support"),
    path('restaurant_api/',RESTAURANT.as_view()),#для преобразования класса в функцию необходимо as_view()
    path('search_restaurant/<pk>',Search_RESTAURANT.as_view()),#<pk> primarykey служит в роли id
    path('users/', UserCreateView.as_view(), name='create_user'),
    path('add_record/', save_request_token, name='add_record'),
    path('api_page/',api_page,name="api_page"),
    path('api_page_2/',api_page_2,name="api_page_2"),




]+router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







