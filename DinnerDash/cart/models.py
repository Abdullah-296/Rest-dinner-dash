from django.db import models
from django.contrib.auth.models import User
from maindisplay.models import *

orderstatus = (
    ('cart', 'cart'),
    ('ordered', 'ordered'),
    ('paid', 'paid'),
    ('cancelled', 'cancelled'),
    ('completed', 'completed'),
)


class Order(models.Model):
    date_ordered = models.DateTimeField(null=True, blank=True)
    date_Paid = models.DateTimeField(null=True, blank=True)
    date_Completed = models.DateTimeField(null=True, blank=True )

    status = models.CharField("order status",
                              max_length=20,
                              choices=orderstatus,
                              default='cart'
                              )

    customer = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 help_text='User Detail',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return "{id}: {customer}".format(id=self.id, customer=self.customer)

    @property
    def item_count(self):
        return self.orderitemsaccess.all().count()

    @property
    def item_quantity_count(self):
        orderitems = self.orderitemsaccess.all()
        return sum([orderitem.quantity for orderitem in orderitems])

    @property
    def price_total(self):
        orderitems = self.orderitemsaccess.all()
        return sum([orderitem.orderitemprice for orderitem in orderitems])


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='orderitemsaccess')
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{id}: {order}=> {item}".format(id=self.id, order=self.order, item=self.item)

    @property
    def orderitemprice(self):
        return self.item.price * self.quantity
