from django.contrib import admin

from maindisplay.models import *


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 3


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline, ]


admin.site.register(Item, ItemAdmin)


admin.site.register(Category)
# admin.site.register(Item)
admin.site.register(Restaurant)
