# [Dinner Dash](https://food-bear.herokuapp.com/) 



This is online food ordering platform (written in Django), where user can visit multiple restaurants, explore items add them to cart and order them.
[link to site](https://food-bear.herokuapp.com/)
## run local server 
Make sure you have 
1. Django 
2. python
 
To run on local server.

After that fork the repository in your local system and
run following command in terminal.

```
pip install -r requirements.txt
```

This will install all the dependencies of project.

1. To run the project, write

```
python3 manage.py runserver
```
2. Go to browser and write following to access the site
```
localhost:8000
```

4. To make super user to access admin

```
python3 manage.py createsuperuser
```

## Features 

### 1. Unauthenticated user can do following:
  * Browse all items, items in particular restaurant
  * Browse items by category
  * Add an item to my cart (only one restaurant  at a time)
  * View my cart
  * Remove an item from my cart
  * Increase the quantity of a item in my cart
  * Log in, which does not clear the cart
  * Clear the cart (Remove all selected items)
  * See popular item (Item that has most order count)

### 2. Authenticated Users
  * log out
  * Their cart is synced across sessions(if they log-out log back in from other device)
  * view their past orders with links to display each order

### 3. Administrator 
   * Create item listings including a name, description, price, and upload photos
   * Create different restaurants
   * Create items according to different restaurants
   * Modify existing items’ name, description, price, and photos
   * Create named categories for items (eg: "Small Plates")
   * Assign items to categories or remove them from categories. Products can belong to more than one category.
   * Retire an item from being sold, which hides it from browsing by any non-administrator
   * Dashboard where he can view all orders
 
