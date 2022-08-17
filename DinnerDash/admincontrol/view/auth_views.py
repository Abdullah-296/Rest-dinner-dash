from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import redirect
from cart.models import Order, OrderItem
from admincontrol.forms import *
from django.contrib.auth.models import User
from maindisplay.models import Item
from django.contrib import messages


class RegisterUser(UserPassesTestMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = "formtemplate.html"

    def test_func(self):
        if self.request.user.is_authenticated:
            return False
        else:
            return True

    def handle_no_permission(self):
        return redirect('homepage')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["formtitle"] = "Signup User"
        data["button"] = "register"
        return data


class LoginUser(LoginView):
    authentication_form = UserLoginForm
    template_name = 'formtemplate.html'
    next_page = reverse_lazy('homepage')
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["formtitle"] = "Login"
        data["buttonname"] = "login"
        return data

    def post(self, request, *args, **kwargs):
        postrequest = super().post(request, *args, **kwargs)

        if request.user.is_authenticated:
            if 'cartdata' in request.session:
                try:
                    user = User.objects.get(id=request.user.id)
                except(User.DoesNotExist, User.MultipleObjectsReturned):
                    user = None

                if user is not None:
                    order, create = Order.objects.get_or_create(customer=user, status='cart')
                    cartdata = request.session['cartdata']

                    queryset = order.orderitem_set.all()
                    restaurantid_previous = 0
                    if queryset.exists():
                        restaurantid_previous = order.orderitem_set.all().first().item.restaurant.id

                    for item in cartdata:
                        if item != 'total':
                            try:
                                iteminstance = Item.objects.get(id=item)

                            except(Item.DoesNotExist, Item.MultipleObjectsReturned):
                                iteminstance = None

                            if user is not None:
                                restaurantid_neworder = iteminstance.restaurant.id

                                if (restaurantid_previous != restaurantid_neworder) and (restaurantid_previous != 0):
                                    messages.success(request, 'Cant add order from different restaurant')

                                else:
                                    orderItem, created = OrderItem.objects.get_or_create(order=order, item=iteminstance)
                                    orderItem.quantity = (orderItem.quantity + int(cartdata[item]['item_quantity']))
                                    orderItem.save()
        return postrequest


class Logout(LogoutView):
    next_page = reverse_lazy('homepage')


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    login_url = reverse_lazy('login')
    template_name = 'formtemplate.html'
    success_url = reverse_lazy('homepage')
