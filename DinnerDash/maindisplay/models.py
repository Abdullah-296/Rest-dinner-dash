from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Restaurant(models.Model):
    Name = models.CharField("Restaurant Name",
                            max_length=30,
                            help_text='Enter Your Restaurant Name',
                            unique=True)

    Address = models.TextField("Restaurant Address",
                               max_length=100,
                               help_text='Enter Your Restaurant Address.')

    Owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              help_text="Enter your Owner Name",
                              related_name='restaurantowner',
                              null=True)

    description = models.TextField("Description",
                                   max_length='150',
                                   null=False,
                                   blank=False,
                                   help_text='Write some description.')

    photo = CloudinaryField("Image",
                            help_text='Upload image of your Restaurant',
                            default='https://res.cloudinary.com/dzag0ldw1/image/upload/v1659178532/gakiweohz9yqelxpbas0.webp',
                            blank=True)

    def __str__(self):
        return self.Name


class Category(models.Model):
    Name = models.CharField("Category Name",
                            max_length=30,
                            help_text='Enter Your Category Name here.',
                            unique=True)

    RestaurantCategory = models.ManyToManyField(
        Restaurant
    )

    def __str__(self):
        return self.Name


class Item(models.Model):
    title = models.CharField("Title",
                             max_length=30,
                             unique=True,
                             null=False,
                             blank=False,
                             help_text='Write title of your item')

    description = models.TextField("Description",
                                   max_length='150',
                                   null=False,
                                   blank=False,
                                   help_text='Write some description.')

    price = models.PositiveIntegerField("Price",
                                        null=False,
                                        blank=False,
                                        help_text='Enter Price')

    category = models.ManyToManyField(
                                 Category,
                                 help_text='link your item to category')

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurantitem')

    order_count = models.PositiveIntegerField("Item Order Count", default=0)

    available = models.BooleanField("Item Available", default=True)

    def __str__(self):
        return self.title


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    photo = CloudinaryField("Image",
                            help_text='Upload image of your item',
                            default='https://res.cloudinary.com/dzag0ldw1/image/upload/v1659178532/gakiweohz9yqelxpbas0.webp',
                            blank=True)

