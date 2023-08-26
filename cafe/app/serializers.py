from rest_framework import serializers
from .models import *
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User




class RestaurantSerializer(serializers.ModelSerializer):# сериализатор для просмотра записей
    class Meta:
        model=Restaurant
        fields=['id','Name_restaurant',"Address","rating","about",'terrace_restaurant',
                'parking_restaurant','kitchen','average_check','email',"phone",'to_publish']


class UserSerializer(serializers.ModelSerializer):# создание нового пользователя
    class Meta:
        model = User
        fields = ['username', "email",'password']
        extra_kwargs = {'password': {'write_only': True}}#отсутствмие отображения пароля после создания 
        

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','Name_restaurant',"Address","rating","about",'terrace_restaurant',
                'parking_restaurant','kitchen','average_check','email',"phone","photo_restaurant", "photo_restaurant2","photo_restaurant3"]
        read_only_fields=["owner_cafe"]#только чтение , автоматически добавляется из за perform_create

class application_doc(serializers.ModelSerializer):
    class Meta:
        model=application_new_restaurant
        fields=['id',"name_new_restaurant","blank","document1","document2","document3"]
        read_only_fields=['user']