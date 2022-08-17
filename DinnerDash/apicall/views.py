from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apicall.serializer import *
from apicall.pagination import CustomPagination
from maindisplay.models import Item, Restaurant
from cart.models import Order
from django.contrib.auth.models import User


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class OrderDisplay(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)

    queryset = Order.objects.all()
    serializer_class = OrderviewSerializer


class ItemDetailRest(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RestaurantDetailRest(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantdetailSerializer


class DisplayRestaurantRest(generics.ListCreateAPIView):
    pagination_class = CustomPagination
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantviewSerializer