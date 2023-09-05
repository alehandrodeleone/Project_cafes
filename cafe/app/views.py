from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login





def start_page(request):
    # Restaurant.objects.all().delete()
    page_number = int(request.GET.get('page', 1))# СТРАНИЦА ПО УМОЛЧАНИЮ ЕСЛИ ОСТУТСТВУЕТ АДРЕС ПАГИНАЦИИ
    back_img = ui_elements.objects.all()# ПОЛУЧАЕМ ВСЕ ИЗОБРАЖЕНИЯ ДЛЯ UI ИЗ БД
    restaurant_info = Restaurant.objects.filter(to_publish=True)# Получаем информацию о ресторанах
    paginator = Paginator(restaurant_info, 1)
    page = paginator.get_page(page_number)
    # current_url = request.build_absolute_uri()  # ПОЛУЧЕНИЕ ТЕКУЩЕЙ ССЫЛКИ
    context = {'page': page,
               'back_img': back_img,
               }
    return render(request, "home_page.html", context)

def start_page_pagination_style2(request):
    # Restaurant.objects.all().delete()
    page_number = int(request.GET.get('Page', 1))# СТРАНИЦА ПО УМОЛЧАНИЮ ЕСЛИ ОСТУТСТВУЕТ АДРЕС ПАГИНАЦИИ
    back_img = ui_elements.objects.all()# ПОЛУЧАЕМ ВСЕ ИЗОБРАЖЕНИЯ ДЛЯ UI ИЗ БД
    restaurant_info = Restaurant.objects.filter(to_publish=True)# Получаем информацию о ресторанах
    paginator = Paginator(restaurant_info, 4)
    page = paginator.get_page(page_number)
    
    # current_url = request.build_absolute_uri()  # ПОЛУЧЕНИЕ ТЕКУЩЕЙ ССЫЛКИ
    context = {'page': page,
               'back_img': back_img,
               }
    return render(request, "HomePage.html", context)

def save_data(request):
    previous_url = request.META.get('HTTP_REFERER')#ПОЛУЧЕНИЕ ПРЕДЫДУЩЕЙ СТРАНИЦЫ ДЛЯ ПЕРЕДАЧИ ЕЕ В АДРЕС ДЛЯ ПОСЛЕДУЮЩЕЙ ПАГИНАЦИИ
    print(previous_url)
    restaurant_info = Restaurant.objects.all()
    back_img = ui_elements.objects.all()
    context = {'back_img': back_img,
               'restaurant': restaurant_info,
               }
    url = requests.get(previous_url).content# ПОЛУЧАЕМ АДРЕС ДЛЯ ПАРСИНГА
    soup = BeautifulSoup(url, 'html.parser')#ПЕРЕДАЕМ АДРЕС В BS И ВЫБИРАЕМ ПАРСЕР
    h2_list = soup.find('h2', {'class': 'name_restaurant'}).text# ИЩЕМ НЕОБХОДИМУЮ ИНФОРМАЦИЮ
    # РЕАЛИЗАЦИЯ ПАРСЕРА ВМЕСТО ЗАПРОСОВ REQUEST

    if request.method == 'POST':
        input1 = request.POST.get('input-booking')
        input2 = request.POST.get('input-number_booking')
        input3 = request.POST.get('input-people_booking')
        
        # Поиск ресторана, у которого Name_restaurant совпадает с restaurant из формы
        restaurant_match = Restaurant.objects.get(Name_restaurant=h2_list)
        
        # Получение пользователя, связанного с найденным рестораном
        user_match = restaurant_match.owner_cafe
        a = booking(name=input1, number=input2, places=input3, restaurant=h2_list, user_booking=user_match)
        a.save()
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'complete.html', context)


def save_data2(request):
    previous_url = request.META.get('HTTP_REFERER')#ПОЛУЧЕНИЕ ПРЕДЫДУЩЕЙ СТРАНИЦЫ ДЛЯ ПЕРЕДАЧИ ЕЕ В АДРЕС ДЛЯ ПОСЛЕДУЮЩЕЙ ПАГИНАЦИИ
    print(previous_url)
    restaurant_info = Restaurant.objects.all()
    back_img = ui_elements.objects.all()
    context = {'back_img': back_img,
               'restaurant': restaurant_info,
               }


    if request.method == 'POST':
        input1 = request.POST.get('input-booking')
        input2 = request.POST.get('input-number_booking')
        input3 = request.POST.get('input-people_booking')
        input4 = request.POST.get('name_restaurant')
        
        # Поиск ресторана, у которого Name_restaurant совпадает с restaurant из формы
        restaurant_match = Restaurant.objects.get(Name_restaurant=input4)
        
        # Получение пользователя, связанного с найденным рестораном
        user_match = restaurant_match.owner_cafe
        a = booking(name=input1, number=input2, places=input3, restaurant=input4, user_booking=user_match)
        a.save()
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'complete.html', context)

def register(request):
    user=request.user
    back_img = ui_elements.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу успешной регистрации
    else:
        form = RegistrationForm()
    context={
        "user":user,
        'form': form,
        'back_img': back_img,
    }
    return render(request, 'Registration_new_user.html', context)


def login_view(request):
    back_img = ui_elements.objects.all()
    context={
        'back_img': back_img,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_page')
        else:
            messages.error(request, 'Неверный логин или пароль')
            return redirect('login')
    return render(request, 'authorization.html', context)


def user_page(request):
    page_number = int(request.GET.get('user_page', 1))  # СТРАНИЦА ПО УМОЛЧАНИЮ ЕСЛИ ОСТУТСТВУЕТ АДРЕС ПАГИНАЦИИ
    restaurant_info = Restaurant.objects.filter(to_publish=True)  # Получаем информацию о ресторанах
    paginator = Paginator(restaurant_info, 1)
    page = paginator.get_page(page_number)
    back_img=ui_elements.objects.all()
    user = request.user# БЕРЕМ ДАННЫЕ ЮЗЕРА И ПЕРЕДАЕМ ИХ В РЕКВЕСТ ДЛЯ ПОСЛЕДУЮЩЕГО ИСПОЛЬЗОВАЕНИЯ
    context={
        "back_img":back_img,
        "user_login":user.username,
        "user_page":page
    }
    return render(request,"user_page.html",context)
def user_page2(request):
  #   page_number = int(request.GET.get('UserPage', 1))  # СТРАНИЦА ПО УМОЛЧАНИЮ ЕСЛИ ОСТУТСТВУЕТ АДРЕС ПАГИНАЦИИ
  # # Получаем информацию о ресторанах
  #   restaurant_info = Restaurant.objects.filter(to_publish=True)# Получаем информацию о ресторанах
  #   paginator = Paginator(restaurant_info, 4)
  #   page = paginator.get_page(page_number)
  #   back_img=ui_elements.objects.all()
  #   user = request.user# БЕРЕМ ДАННЫЕ ЮЗЕРА И ПЕРЕДАЕМ ИХ В РЕКВЕСТ ДЛЯ ПОСЛЕДУЮЩЕГО ИСПОЛЬЗОВАЕНИЯ
  #   context={
  #       "back_img":back_img,
  #       "user_login":user.username,
  #       "user_page":page
  #   }
  #   return render(request,"UserPage.html",context)

    page_number = int(request.GET.get('Page', 1))  # СТРАНИЦА ПО УМОЛЧАНИЮ ЕСЛИ ОСТУТСТВУЕТ АДРЕС ПАГИНАЦИИ
    back_img = ui_elements.objects.all()  # ПОЛУЧАЕМ ВСЕ ИЗОБРАЖЕНИЯ ДЛЯ UI ИЗ БД
    restaurant_info = Restaurant.objects.filter(to_publish=True)  # Получаем информацию о ресторанах
    paginator = Paginator(restaurant_info, 4)
    page = paginator.get_page(page_number)
    user = request.user
    # current_url = request.build_absolute_uri()  # ПОЛУЧЕНИЕ ТЕКУЩЕЙ ССЫЛКИ
    context = {'page': page,
               'back_img': back_img,
               "user_login": user.username,

               }
    return render(request, "UserPage.html", context)


def setting_user(request):
    back_img=ui_elements.objects.all()
    res = Restaurant.objects.all()
    user = request.user
    context={
        "back_img":back_img,
        "user":user,
        "res":res,
    }
    return render(request,"setting_user.html",context)


def application_new_res(request):
    back_img = ui_elements.objects.all()
    user = request.user
    new_restaurant = application_new_restaurant.objects.all()
    info=info_text.objects.filter(id=1)
    context={
        "back_img":back_img,
       "new_restaurant":new_restaurant,
        "user":user,
        "info":info
    }
    return render (request,"application_new_restaurant.html",context)


def save_application(request):
    previous_url = request.META.get('HTTP_REFERER')#ПОЛУЧЕНИЕ ПРЕДЫДУЩЕЙ СТРАНИЦЫ ДЛЯ ПЕРЕДАЧИ ЕЕ В АДРЕС ДЛЯ ПОСЛЕДУЮЩЕЙ ПАГИНАЦИИ
    print(previous_url)
    restaurant_info = Restaurant.objects.all()
    user = request.user
    back_img = ui_elements.objects.all()
    application = application_new_restaurant.objects.all()
    context = {'back_img': back_img,
               'restaurant': restaurant_info,
               "user": user,
               "application":application
               }
    if request.method == 'POST':#ПОЛУЧАЕМ ИНФОРМАЦИЮ ИЗ HTML ЗАПРОСОВ
        input1 = request.POST.get('name_restaurant_input')
        input2 = request.FILES.get('myfile1')
        input3 = request.FILES.get('myfile2')
        input4 = request.FILES.get('myfile3')
        input5 = request.FILES.get('myfile4')
        input6 = request.POST.get("name_restaurant_input_post")
        input7 = request.POST.get("adress_input_post")
        input8 = request.POST.get("terrace_input_post")
        input9 = request.POST.get("parking_input_post")
        input10 = request.POST.get("kitchen_input_post")
        input11 = request.POST.get("average_check_input_post")
        input12 = request.POST.get("email_input_post")
        input13 = request.POST.get("number_input_post")
        input14 = request.POST.get("about")
        input15 = request.FILES.get('photo_restaurant')
        input16 = request.FILES.get('photo_restaurant2')
        input17 = request.FILES.get('photo_restaurant3')
        input18 = request.FILES.get('menu_download')
        a = application_new_restaurant(name_new_restaurant=input1, blank=input2, document1=input3, document2=input4,document3=input5,user=user)# сохранение данных из инпутов в модель джанго
        a.save()
        b = Restaurant(Name_restaurant=input6,Address=input7,terrace_restaurant=input8,parking_restaurant=input9,
                     kitchen=input10,average_check=input11,email=input12,phone=input13,about=input14,photo_restaurant=input15,
                     photo_restaurant2=input16,photo_restaurant3=input17,menu_download=input18)
        b.save()
        return HttpResponseRedirect(request.path_info)
    return render(request, 'complete_application.html', context)


def edit_restaurant(request):
    back_img = ui_elements.objects.all()
    user = request.user
    restaurant = get_object_or_404(Restaurant, owner_cafe=user)
    info=info_text.objects.filter(id=2)
    if request.method == 'POST':
        initial_data = {'to_publish': False}
        form = edit_restaurantForm(request.POST, instance=restaurant,initial=initial_data)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.to_publish = False
            instance.save()
            form.save()
        return redirect('complete_page')
    else:
        form = edit_restaurantForm(request.POST,instance=Restaurant)
    context = {
        'form': form,
        "back_img":back_img,
        "user":user,
        "info":info
    }
    return render(request, 'edit_restaurant.html', context)


def profile_and_mail(request):
    user = request.user
    bookings=booking.objects.filter(user_booking=user)
    message_info = message.objects.filter(message_user=user)  # Получаем информацию о ресторанах
    back_img = ui_elements.objects.all()
    Request_token =request_token.objects.filter(request_token_user=user)
    context = {
        "user": user,
        "back_img": back_img,
        "profile": message_info,
        "booking":bookings,
        "req_token_user":Request_token
    }
    
        
    return render(request, "profile.html", context)


def save_request_token(request):
    user = request.user
    Request_token =request_token.objects.filter(request_token_user=user)
    context = {
        "user": user,
        "req_token_user":Request_token
    }
    Request_token_save=request_token(request_token_user=user)
    Request_token_save.save()

    return render(request, "complete_application.html", context)


def support(request):
    user=request.user
    back_img = ui_elements.objects.all()
    message_support=support_message.objects.all()
    info=info_text.objects.filter(id=3)
    form = support_messageForm(request.POST)
    if request.method == 'POST':
        form = support_messageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)#commit=False позволяет создать экземпляр модели, но не сохранять его.
            instance.application_user = user # Присваиваем текущего пользователя полю "application_user"
            instance.save()#instance - это переменная, которая содержит созданный экземпляр модели и позволяет вам выполнять дополнительные действия с ним перед сохранением в базе данных.
            return redirect('complete_page') 
        else:
            form = support_messageForm()
    context = {
        "info":info,
        "user": user,
        "back_img": back_img,
        "message": message_support,
        'form': form,
    }
    return render(request,"support.html",context)


def complete_html(request):
    user = request.user
    context = {
               "user": user
               }
    return render(request, 'complete_application.html', context)


def api_page(request):
    back_img=ui_elements.objects.all()
    user=request.user
    context={
        "back_img":back_img,
        "user":user
    }
    return render(request,"api_page.html",context)


def api_page_2(request):
    back_img=ui_elements.objects.all()
    user=request.user
    context={
        "back_img":back_img,
        "user":user
    }
    return render(request,"api_page_2.html",context)


def tg_page(request):
    back_img=ui_elements.objects.all()
    user=request.user
    context={
        "back_img":back_img,
        "user":user
    }
    return render(request,"TG.html",context)


def about_project_page(request):
    user=request.user
    back_img=ui_elements.objects.all()
    context={
        "back_img":back_img,
        "user":user
    }
    return render(request,"about_project.html",context)


# //////////////////////////////////////////////////////////API//////////////////////////////////////////////////////////////
from .serializers import *
from rest_framework.generics import *
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import *



# /////////////////////////////////////////
class RESTAURANT(ListAPIView):# Получение списков ресторанов
    queryset = Restaurant.objects.all()#список обьектов
    serializer_class = RestaurantSerializer # то с помощью чего мы превращаем список обьектов в json
    filterset_fields=['Name_restaurant',"Address","rating","about",'terrace_restaurant',
                'parking_restaurant','kitchen','average_check','email',"phone",'to_publish']#список для фильтрации
    pagination_class = LimitOffsetPagination
# /////////////////////////////////////////

class Search_RESTAURANT(RetrieveAPIView):#Поиск ресторана по id
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UserCreateView(generics.CreateAPIView):#создание нового юзера
    queryset = User.objects.all()
    serializer_class = UserSerializer

# /////////////////////////////////////////
class  work_with_restaurant(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated,RestaurantPermission]#Аутентификация по токену и разрешения permission
    def perform_create(self, serializer):
        serializer.save(owner_cafe=self.request.user)# создание записи от лица владельца токена
        
class application_new_restauran_doc(ModelViewSet):
    queryset = application_new_restaurant.objects.all()
    serializer_class = application_doc
    permission_classes = [IsAuthenticated,application_doc_Permission]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)