
from .models import *
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import *


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


    if request.method == 'POST':#ПОЛУЧАЕМ ИНФОРМАЦИЮ ИЗ HTML ЗАПРОСОВ
        input1 = request.POST.get('input-booking')
        input2 = request.POST.get('input-number_booking')
        input3 = request.POST.get('input-people_booking')

        a = booking(name=input1, number=input2, places=input3, restaurant=h2_list)# сохранение данных из инпутов в модель джанго
        a.save()

        return HttpResponseRedirect(request.path_info)

    return render(request, 'complete.html', context)




def register(request):

    back_img = ui_elements.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success/')  # Перенаправление на страницу успешной регистрации
    else:
        form = RegistrationForm()

    context={
        'form': form,
        'back_img': back_img,

    }
    return render(request, 'Registration_new_user.html', context)

from django.contrib.auth import authenticate, login

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
            return HttpResponse('Invalid login credentials')
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
        a = application_new_restaurant(name_new_restaurant=input1, blank=input2, document1=input3, document2=input4,document3=input5)# сохранение данных из инпутов в модель джанго
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
    }
    return render(request, 'edit_restaurant.html', context)

def complete_html(request):

    user = request.user
   
    context = {
               "user": user
               }

    return render(request, 'complete_application.html', context)
