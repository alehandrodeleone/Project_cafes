from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from app.views import start_page,save_data,registration,registration_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',start_page,name="start_page"),
    path('complete/', save_data, name='save_data'),
    path('registration/',registration,name="registration"),
    path('reg_complete/',registration_complete,name="registration_complete")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('complete/', save_data, name='save_data'),