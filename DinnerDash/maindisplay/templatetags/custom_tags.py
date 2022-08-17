from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from cart.models import *

register = template.Library()


@register.filter(name="has_prev")
def has_prev(user):
    for order in user.order_set.all():
        if order.status != 'cart':
            return True
    return False


@register.filter(name="category_count")
def category_count(category):
    return Order.objects.filter(status=category).count()


@register.filter(name="specific_order")
def specific_order(category):
    return Order.objects.filter(status=category).order_by("-id")[:20]


@register.filter(name="cart_order_count")
def cart_order_count(user):
        cart_order = user.order_set.filter(status='cart')
        if cart_order.exists():
            return cart_order.first().item_count
        else:
            return 0


@register.filter(name="cart_order_item_count")
def cart_order_item_count(user):
    cart_order = user.order_set.filter(status='cart')
    if cart_order.exists():
        return cart_order
    else:
        return None
