from rest_framework import serializers
from maindisplay.models import Restaurant, Item, ItemImage

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from cart.models import Order, OrderItem


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True)
    class Meta:
        model = Item
        fields = "__all__"




class RestaurantdetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, source='restaurantitem')

    class Meta:
        model = Restaurant
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderviewSerializer(serializers.ModelSerializer):
    # items = OrderItemSerializer(many=True, source='orderitems')
    items = OrderItemSerializer(many=True, source='orderitemsaccess')

    class Meta:
        model = Order
        fields = "__all__"


class RestaurantviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        min_length=2,
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True,
                                     required=True,
                                     validators=[validate_password],
                                     min_length=8,
                                     max_length=32)
    password2 = serializers.CharField(write_only=True,
                                      required=True,
                                      min_length=8,
                                      max_length=32)

    # first_name = serializers.CharField(write_only=True,
    #                                    required=True,
    #                                    min_length=2,
    #                                    max_length=32)
    #
    # last_name = serializers.CharField(write_only=True,
    #                                   required=True,
    #                                   min_length=2,
    #                                   max_length=32)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
