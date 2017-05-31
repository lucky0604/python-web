# Cart class that will allow to manage the shopping cart
from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    def __init__(self, request):
        # initialize the cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # add products to the cart or update their quantity
    def add(self, product, quantity = 1, update_quantity = False):
        # add a product to the cart or update its quantity
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # make the session as 'modified' to make sure it is saved
        self.session.modified = True

    # removing products from the cart
    def remove(self, product):
        # remove a product from the cart
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # iterate through the items contained in the cart and access the related Product instance
    def __iter__(self):
        # Iterate over the items in the cart and get the products from the database
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in = product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # the len() function is executed on an object, Python calls ites __len__() method to retrieve its length
    # define a custom __len__() method to return the total number of items stored in the cart
    def __len__(self):
        # count all items in the cart
        return sum(item['quantity'] for item in self.cart.values())

    # calculate the total cost for the items in the cart
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # clear the cart session
    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
