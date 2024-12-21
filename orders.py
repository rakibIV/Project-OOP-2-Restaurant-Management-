from products import Product
class Order:
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
        self.total = 0
        for product in Product.products:
            if product.name.lower() == self.name.lower():
                if product.quantity >= quantity:
                    self.total = product.price * quantity
                    product.quantity -= quantity
                break
        