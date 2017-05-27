# setting the cart into the requestcontext
from .cart import Cart
def cart(request):
    return {'cart': Cart(request)}
