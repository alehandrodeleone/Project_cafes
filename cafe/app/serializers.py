from rest_framework import serializers
from .models import *
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User




class RestaurantSerializer(serializers.ModelSerializer):# сериализатор для просмотра записей
    class Meta:
        model=Restaurant
        fields=['id','Name_restaurant',"Address","rating","about",'terrace_restaurant',
                'parking_restaurant','kitchen','average_check','email',"phone",'to_publish']

class New_RestaurantSerializer(serializers.ModelSerializer):# сериализатор для создания записи
    class Meta:
        model=Restaurant
        fields=['id',"owner_cafe",'Name_restaurant',"Address","rating","about",'terrace_restaurant',
                'parking_restaurant','kitchen','average_check','email',"phone","photo_restaurant","photo_restaurant2","photo_restaurant3","menu_download"]
        read_only_fields = ['owner_cafe']#необходимо для скрытия данного поля и для отсутствия возможности создания записи под другим пользователем
#perform_create во вьюхе автоматически заполняет поле по токену
class UserSerializer(serializers.ModelSerializer):# создание нового пользователя
    class Meta:
        model = User
        fields = ['username', "email",'password']
        extra_kwargs = {'password': {'write_only': True}}#отсутствмие отображения пароля после создания 









        

        # class RestaurantSerializer(serializers.Serializer):
        #     Name_restaurant = serializers.CharField()#отмечаю что в сериализваторе необходимо использовать для отображения serializers.Charfield
        #     Address = serializers.CharField()
        #     rating = serializers.IntegerField()
        #     about = serializers.CharField()
        #     terrace_restaurant = serializers.CharField()
        #     parking_restaurant = serializers.CharField()
        #     kitchen = serializers.CharField()
        #     average_check = serializers.IntegerField()
        #     email = serializers.EmailField()
        #     phone = serializers.CharField()#в сериализаторе в отличии от модели PhoneNumberField необходимо переназначить как строк, а именно в charfield
        #     to_publish = serializers.BooleanField()