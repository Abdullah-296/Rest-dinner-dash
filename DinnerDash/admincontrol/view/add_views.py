from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
import cloudinary
from maindisplay.forms import AddItemform, AddRestaurantform, AddCategoryform
from admincontrol.view.dashboard_views import CheckStaffUser
from maindisplay.models import *
from django.contrib import messages


class BaseAdd(UserPassesTestMixin, CreateView):
    template_name = 'formtemplate.html'
    success_url = reverse_lazy('homepage')

    def test_func(self):
        if self.request.user.is_staff:
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect('homepage')


class AddRestaurant(BaseAdd):
    model = Restaurant
    form_class = AddRestaurantform

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["formtitle"] = "Add Restaurant"
        data["buttonname"] = "Add"
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Restaurant added successfully')
        form.save()
        return super().form_valid(form)


class AddCategory(BaseAdd):
    model = Category
    form_class = AddCategoryform

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["formtitle"] = "Add Category"
        data["buttonname"] = "Add"
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Category added successfully')
        form.save()
        return super().form_valid(form)


class UpdateItem(CheckStaffUser, UpdateView ):
    template_name = 'formtemplate.html'
    form_class = AddItemform
    model = Item
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["formtitle"] = "Update Item"
        data["buttonname"] = "Update"
        return data

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:
            if self.request.FILES:
                for image in self.request.FILES.getlist('images'):
                    file = cloudinary.uploader.upload(image.file)
                    ItemImage.objects.create(item=self.object, photo=file['url'])
            else:
                ItemImage.objects.create(item=self.object)
        return response

    def form_valid(self, form):
        messages.success(self.request, 'Item updated successfully')
        form.save()
        return super().form_valid(form)


class AddItem(BaseAdd):
    form_class = AddItemform

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["formtitle"] = "Add Item"
        data["buttonname"] = "Add"
        return data

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:
            if self.request.FILES:
                for image in self.request.FILES.getlist('images'):
                    file = cloudinary.uploader.upload(image.file)
                    ItemImage.objects.create(item=self.object, photo=file['url'])
            else:
                ItemImage.objects.create(item=self.object)
        return response

    def form_valid(self, form):
        messages.success(self.request, 'Item added to particular restaurant successfully')
        form.save()
        return super().form_valid(form)
