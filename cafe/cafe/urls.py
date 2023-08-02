from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from app.views import start_page,save_data,register,login_view,user_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',start_page,name="start_page"),
    path('complete/', save_data, name='save_data'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path("user_page/",user_page,name="user_page")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('complete/', save_data, name='save_data'),