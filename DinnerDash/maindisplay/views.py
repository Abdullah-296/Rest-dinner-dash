from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from maindisplay.models import *
from django.shortcuts import render






class DisplayRestaurant(ListView):
    paginate_by = 15
    model = Restaurant
    template_name = 'multipleitemtemplate.html'
    context_object_name = "items"

    def get_queryset(self):
        return super().get_queryset().order_by("id")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["page"] = "Restaurant"
        return data


class ItemDetail(DetailView):
    model = Item
    template_name = 'itemdetail.html'
    context_object_name = "item"


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'multipleitemtemplate.html'
    context_object_name = "Ritems"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['selected_category'] = self.request.GET.get('itemcategory', 'all')
        page = self.request.GET.get('page', 1)

        if data['selected_category'] == 'all':
            itempage = Paginator(Restaurant.objects.get(id=self.object.id).restaurantitem.all(), self.paginate_by)

        elif data['selected_category'] == 'popular':
            itempage = Paginator(
                Restaurant.objects.get(id=self.object.id).restaurantitem.all().order_by('order_count').reverse(),
                self.paginate_by)
        else:
            itempage = Paginator(Restaurant.objects.get(id=self.object.id).restaurantitem.filter(
                category__Name=data['selected_category']), self.paginate_by)

        try:
            data['fitems'] = itempage.page(page)
        except PageNotAnInteger:
            data['fitems'] = itempage.page(1)
        except EmptyPage:
            data['fitems'] = itempage.page(1)

        return data


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
