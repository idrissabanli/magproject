from rest_framework.serializers import ModelSerializer
from magapp.models import Product, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'image',
        ]

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
        ]

class ProductReadSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    owner = UserProfileSerializer()

    class Meta:
        model = Product
        fields = [ # '__all__'
            'id',
            'owner',
            'category',
            'tags',
            'product_name',
            'price',
            'discountprice',
            'description',
            'author',
            'pagecount',
            'created_at',
        ]


class ProductCreateSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = [ # '__all__'
            'id',
            'owner',
            'category',
            'tags',
            'product_name',
            'price',
            'discountprice',
            'description',
            'author',
            'pagecount',
            'created_at',
        ]


