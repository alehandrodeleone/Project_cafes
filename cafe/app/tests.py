from django.test import TestCase

# Create your tests here.
class New_RestaurantSerializer(serializers.ModelSerializer):# сериализатор для создания записи
    class Meta:
        model=Restaurant
        fields=['id',"owner_cafe",'Name_restaurant',"Address","rating","about",'terrace_restaurant',
                'parking_restaurant','kitchen','average_check','email',"phone","photo_restaurant","photo_restaurant2","photo_restaurant3","menu_download"]
        read_only_fields = ['owner_cafe']#необходимо для скрытия данного поля и для отсутствия возможности создания записи под другим пользователем
#perform_create во вьюхе автоматически заполняет поле по токену
