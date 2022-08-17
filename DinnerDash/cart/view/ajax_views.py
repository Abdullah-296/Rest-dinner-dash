from django.http import JsonResponse
import json
from cart.models import *
from maindisplay.models import *
import datetime
from django.views import View


class OrderstatusAjax(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        orderid = data['OrderId']
        action = data['action']

        try:
            orderobject = Order.objects.get(id=orderid)
        except(Order.DoesNotExist, Order.MultipleObjectsReturned):
            orderobject = None

        if orderobject is not None:
            if action == 'paid':
                orderobject.status = 'paid'
                orderobject.date_Paid = datetime.datetime.now()

            elif action == 'cancel':
                orderobject.status = 'cancelled'

            elif action == 'complete':
                orderobject.status = 'completed'
                orderobject.date_Completed = datetime.datetime.now()

            orderobject.save()
            return JsonResponse("Accept", safe=False)
        return JsonResponse("Reject", safe=False)


class ChangeItemAvailability(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        itemid = data['itemid']
        action = data['action']

        if request.user.is_staff:
            try:
                itemobject = Item.objects.get(id=itemid)
            except(Item.DoesNotExist, Item.MultipleObjectsReturned):
                itemobject = None

            if itemobject is not None:
                if action == 'unavailable':
                    itemobject.available = False
                elif action == 'available':
                    itemobject.available = True
                itemobject.save()
                return JsonResponse("Accept", safe=False)

        return JsonResponse("Reject", safe=False)


class CheckoutAjax(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        orderid = data['Orderid']

        try:
            orderobject = Order.objects.get(id=orderid, status='cart')
        except(Order.DoesNotExist, Order.MultipleObjectsReturned):
            orderobject = None

        if orderobject is not None:
            orderobject.status = 'ordered'
            orderobject.date_ordered = datetime.datetime.now()
            orderobject.save()

            return JsonResponse("Accept", safe=False)

        return JsonResponse("Reject", safe=False)


class SessionCart(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        action = data['action']

        if action == 'CLEARCART':
            items = data['check']
            cart_data = request.session['cartdata']
            for item in items:
                del cart_data[item]

            request.session['cartdata'] = cart_data

        else:
            productid = data['ItemId']
            action = data['action']
            quantity = data['item_quantity']

            try:
                itemobject = Item.objects.values().get(id=productid)
                restaurantid_new = Item.objects.get(id=productid).restaurant.id
                itemobject['photo'] = Item.objects.get(id=productid).images.first().photo.url

            except(Item.DoesNotExist, Item.MultipleObjectsReturned):
                itemobject = None

            if itemobject is not None:
                cart_item = {productid: {
                    'itemobject': itemobject,
                    'item_quantity': quantity,
                    'action': action,
                    'total_price': int(quantity) * int(itemobject['price'])
                }}

                if 'cartdata' in request.session:
                    res = list(request.session['cartdata'].keys())
                    restaurantid_pre = 0
                    if int(len(res)) != 1:
                        if res[0] == 'total':
                            restaurantid_pre = Item.objects.get(id=res[1]).restaurant.id
                        else:
                            restaurantid_pre = Item.objects.get(id=res[0]).restaurant.id

                    if ((restaurantid_pre == restaurantid_new) or (restaurantid_pre == 0)):
                        if (productid in request.session['cartdata']):
                            cart_data = request.session['cartdata']
                            if action == 'ADD':
                                cart_data[productid]['item_quantity'] = str(int(cart_data[productid]['item_quantity']) + 1)
                                cart_data[productid]['total_price'] = str(
                                    int(cart_data[productid]['item_quantity']) * int(
                                        cart_data[productid]['itemobject']['price']))

                            elif action == 'SUB':
                                cart_data[productid]['item_quantity'] = str(int(cart_data[productid]['item_quantity']) - 1)
                                cart_data[productid]['total_price'] = str(
                                    int(cart_data[productid]['item_quantity']) * int(
                                        cart_data[productid]['itemobject']['price']))

                            elif action == 'Remove':
                                del cart_data[productid]

                            request.session['cartdata'] = cart_data

                        else:
                            cart_data = request.session['cartdata']
                            cart_data.update(cart_item)
                            request.session['cartdata'] = cart_data

                    else:
                        return JsonResponse('Reject', safe=False)

                else:
                    request.session['cartdata'] = cart_item

        Total_quantity = 0
        Total_price = 0
        for item in request.session['cartdata']:
            if item != 'total':
                Total_quantity += int(request.session['cartdata'][item]['item_quantity'])
                Total_price += int(request.session['cartdata'][item]['total_price'])

        Total = {'price': Total_price,
                 'quantity': Total_quantity}

        request.session['cartdata']['total'] = Total
        return JsonResponse(request.session['cartdata'], safe=False)


class UpdateItem(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        productid = data['ItemId']
        action = data['action']

        if action == 'Remove':
            try:
                orderitem = OrderItem.objects.get(id=productid)
            except(OrderItem.DoesNotExist, OrderItem.MultipleObjectsReturned):
                orderitem = None

            if orderitem is not None:
                orderitem.delete()
                return JsonResponse("Accept", safe=False)
            return JsonResponse("Reject", safe=False)

        elif action == 'CLEARCART':
            Items = data['check']
            try:
                order = Order.objects.get(id=productid)
            except(Order.DoesNotExist, Order.MultipleObjectsReturned):
                order = None

            if order is not None:
                for i in Items:
                    item = order.orderitem_set.all().filter(item=i)
                    item.delete()

                return JsonResponse("Accept", safe=False)
            return JsonResponse("Reject", safe=False)

        elif action == 'ADDITEMCART':
            try:
                orderitem = OrderItem.objects.get(id=productid)
            except(OrderItem.DoesNotExist, OrderItem.MultipleObjectsReturned):
                orderitem = None

            if orderitem is not None:
                orderitem.quantity = (orderitem.quantity + 1)

                try:
                    item = Item.objects.get(id=orderitem.item.id)
                except(Item.DoesNotExist, Item.MultipleObjectsReturned):
                    item = None

                if item is not None:
                    item.order_count = (item.order_count + 1)
                    item.save()
                    orderitem.save()

                    return JsonResponse("Accept", safe=False)
            return JsonResponse("Reject", safe=False)

        elif action == 'SUBITEMCART':
            try:
                orderitem = OrderItem.objects.get(id=productid)
            except(OrderItem.DoesNotExist, OrderItem.MultipleObjectsReturned):
                orderitem = None

            if orderitem is not None:
                orderitem.quantity = (orderitem.quantity - 1)
                orderitem.save()

                if orderitem.quantity <= 0:
                    orderitem.delete()

                return JsonResponse("Accept", safe=False)
            return JsonResponse("Reject", safe=False)
        else:
            try:
                item = Item.objects.get(id=productid)
            except(Item.DoesNotExist, Item.MultipleObjectsReturned):
                item = None

            if item is not None:
                try:
                    user = User.objects.get(id=request.user.id)
                except(User.DoesNotExist, User.MultipleObjectsReturned):
                    user = None

                if user is not None:
                    order, create = Order.objects.get_or_create(customer=user, status='cart')

                    queryset = order.orderitem_set.all()
                    if queryset.exists():
                        restaurantid_previous = order.orderitem_set.all().first().item.restaurant.id
                        restaurantid_neworder = item.restaurant.id

                        if restaurantid_previous != restaurantid_neworder:
                            return JsonResponse("Reject", safe=False)

                    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)

                    if action == 'ADD':
                        item.order_count = (item.order_count + 1)
                        orderItem.quantity = (orderItem.quantity + 1)

                    elif action == 'remove':
                        orderItem.quantity = (orderItem.quantity - 1)

                    item.save()
                    orderItem.save()

                    return JsonResponse("Accept", safe=False)
                return JsonResponse("Reject")


class GetRestaurantCategory(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        restaurant_id = data['restaurant']

        print(restaurant_id)
        try:
            restaurantinstance = Restaurant.objects.get(id=restaurant_id)
            restaurantcategory = restaurantinstance.category_set.all()

        except(Restaurant.DoesNotExist, Restaurant.MultipleObjectsReturned):
            restaurantcategory = None

        if restaurantcategory is not None:
            print(list(restaurantcategory.values()))
            return JsonResponse(list(restaurantcategory.values()), safe=False)
        else:
            return JsonResponse("Reject", safe=False)




