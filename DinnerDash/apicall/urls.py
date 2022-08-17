from django.urls import path
from apicall import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("api/getrestaurant/", views.DisplayRestaurantRest.as_view(), name='restaurantrest'),
    path("api/getrestaurantdetail/<int:pk>", views.RestaurantDetailRest.as_view(), name='restaurantrestdetail'),
    path("api/getitemdetail/<int:pk>", views.ItemDetailRest.as_view(), name='itemrestdetail'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/orders/', views.OrderDisplay.as_view(), name='ordersdisplay'),
    path('api/registeruser/', views.CreateUser.as_view(), name='createuser'),


]
