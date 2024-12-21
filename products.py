class Product:
    products = []
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.products.append(self)
        
    def update_price(self,price):
        if price > 0:
            self.price = price
            
            
    