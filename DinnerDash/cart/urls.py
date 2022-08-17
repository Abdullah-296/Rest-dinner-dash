from django.urls import path
from cart.view import cart_views, ajax_views

urlpatterns = [
    path("cart/", cart_views.DisplayCart.as_view(), name='cart'),
    path("checkout/", cart_views.CheckOut.as_view(), name='checkout'),
    path("previous_orders/", cart_views.PreviousOrder.as_view(), name='previous_order'),

    path("update_item/", ajax_views.UpdateItem.as_view(), name='updateitem'),
    path("session_cart/", ajax_views.SessionCart.as_view(), name='sessionitem'),
    path("checkout-ajax/", ajax_views.CheckoutAjax.as_view(), name='checkoutajax'),
    path("update_status/", ajax_views.OrderstatusAjax.as_view(), name='orderstatusajax'),
    path("change-availability/", ajax_views.ChangeItemAvailability.as_view(), name='itemavailability'),
    path("get_restaurant_category/", ajax_views.GetRestaurantCategory.as_view(), name='getrestaurantcategory'),


]