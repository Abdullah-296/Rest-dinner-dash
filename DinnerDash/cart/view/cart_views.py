from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class DisplayCart(TemplateView):
    template_name = 'order.html'


class CheckOut(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'checkout.html'


class PreviousOrder(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["page"] = "Previous Order"
        return data
