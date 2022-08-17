from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from cart.models import Order, orderstatus


class CheckStaffUser(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect('homepage')


class OrderDetail(UserPassesTestMixin, DetailView):
    model = Order
    template_name = 'order.html'
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["page"] = "Orderdetail"
        return data

    def test_func(self, **kwargs):
        if self.request.user.is_staff:
            return True
        elif self.request.user.is_authenticated:
            try:
                orderowner_id = Order.objects.get(id=self.kwargs['pk']).customer.id

            except(Order.DoesNotExist, Order.MultipleObjectsReturned):
                orderowner_id = None

            if orderowner_id is not None:
                if self.request.user.id == orderowner_id:
                    return True
        return False

    def handle_no_permission(self):
        return redirect('homepage')


class AdminPanel(CheckStaffUser, ListView):
    model = Order
    template_name = 'multipleitemtemplate.html'
    context_object_name = "orders"
    paginate_by = 15

    def get_queryset(self):
        return super().get_queryset().order_by("-id")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["page"] = "AdminPanel"
        data["categorys"] = [orderstatus[c][0] for c in range(len(orderstatus))]

        data['ordercategory'] = self.request.GET.get('ordercategory', 'all')
        page = self.request.GET.get('page', 1)

        if data['ordercategory'] == 'all':
            data['orders'] = Order.objects.all()
        else:
            itempage = Paginator(Order.objects.filter(
                status=data['ordercategory']), self.paginate_by)
            try:
                data['orders'] = itempage.page(page)
            except PageNotAnInteger:
                data['orders'] = itempage.page(1)
            except EmptyPage:
                data['orders'] = itempage.page(1)
        return data
