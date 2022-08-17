from django.urls import path
from maindisplay import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("", views.DisplayRestaurant.as_view(), name='homepage'),
    path("restaurantitems/<int:pk>", views.RestaurantDetail.as_view(), name='restaurant'),
    path("item/<int:pk>/", views.ItemDetail.as_view(), name='detail'),

]
