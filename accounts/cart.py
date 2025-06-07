from .models import Product  # Make sure to import your Product model

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def get_items(self):
        items = []
        for product_id, quantity in self.cart.items():
            product = Product.objects.get(id=product_id)  # Fetch the product
            items.append({'product': product, 'quantity': quantity})
        return items

    def get_total_price(self):
        total = 0
        for item in self.get_items():
            total += item['product'].price * item['quantity']
        return total

    # Additional methods to add/remove items...
