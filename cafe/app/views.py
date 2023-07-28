from captcha.image import ImageCaptcha
from random import choice
from .models import Restaurant,ui_elements,booking,owner
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.conf import settings
import os
from .forms import RegistrationForm
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

def registration(request):
    # owner.objects.all().delete()
    back_img = ui_elements.objects.all()

    value=["1","q","s","2","H","6","i","L","9","B",'z']
    pattern=[]
    for i in range(5):#выбираем кол-во значений в капче
        pattern.append(choice(value))


    image_captcha=ImageCaptcha(width=300, height=200)##### задаем размеры для изображение
    #image_captcha.write(pattern,'captcha.png')#записываем изображение
    media_path = settings.MEDIA_ROOT#обозначаем корневую папку медиафалов в нашем случае media указано в settings
    image_path = os.path.join(settings.MEDIA_ROOT,'captcha.png')# указываем название
    image_captcha.write(pattern, os.path.join(media_path, image_path))# сохраняем

    context = {
               'back_img': back_img,
                'image_path': image_path,


               }
    return render(request, "registration.html", context)


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