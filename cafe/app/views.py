from captcha.image import ImageCaptcha
from random import choice
from .models import *
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
def start_page(request):
    page_number = int(request.GET.get('page', 1))# СТРАНИЦА ПО УМОЛЧАНИЮ ЕСЛИ ОСТУТСТВУЕТ АДРЕС ПАГИНАЦИИ
    back_img = ui_elements.objects.all()# ПОЛУЧАЕМ ВСЕ ИЗОБРАЖЕНИЯ ДЛЯ UI ИЗ БД
    restaurant_info = Restaurant.objects.all()# Получаем информацию о ресторанах
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
    # User.objects.all().delete()
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
    restaurant_info = Restaurant.objects.all()  # Получаем информацию о ресторанах
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
        input2 = request.POST.get('myfile1')
        input3 = request.POST.get('myfile2')
        input4 = request.POST.get('myfile3')
        input5 = request.POST.get('myfile4')

        a = application_new_restaurant(name_new_restaurant=input1, blank=input2, document1=input3, document2=input4, document3=input5)# сохранение данных из инпутов в модель джанго
        a.save()

        return HttpResponseRedirect(request.path_info)

    return render(request, 'complete.html', context)