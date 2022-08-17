from django.urls import path
from admincontrol.view import add_views, auth_views, dashboard_views

urlpatterns = [

    path("registeruser/", auth_views.RegisterUser.as_view(), name='signup'),
    path("loginuser/", auth_views.LoginUser.as_view(), name='login'),
    path("changepassword/", auth_views.ChangePassword.as_view(), name='changepassword'),
    path("logout/", auth_views.Logout.as_view(), name='logout'),


    path("additem/", add_views.AddItem.as_view(), name='additem'),
    path("addrestaurant/", add_views.AddRestaurant.as_view(), name='addrestaurant'),
    path("addcategory/", add_views.AddCategory.as_view(), name='addcategory'),
    path("updateitem/<int:pk>", add_views.UpdateItem.as_view(), name='updateitem'),


    path("adminpanel/", dashboard_views.AdminPanel.as_view(), name='adminpanel'),
    path("order-detail/<int:pk>", dashboard_views.OrderDetail.as_view(), name='orderdetail'),
]