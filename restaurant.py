from users import Customer,Admin
from orders import Order
from products import Product


class Restaurant:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.menu = Product.products
        
    def view_menu(self):
        print('Menu : ')
        print('----------------Product List----------------')
        print('Name\t Price\t Quantity')
        for product in self.menu:
            print(f'{product.name}\t {product.price}\t    {product.quantity}')
            
    def view_customer_list(self):
        print('Customer List : ')
        print('Name\t Email\t Cur Balance')
        for customer in Customer.customers:
            print(f'{customer.name}\t {customer.email}\t {customer.check_balance}')
            
    def add_to_menu(self,name,price,quantity):
        for product in self.menu:
            if product.name.lower() == name.lower():
                product.quantity += quantity
                return 'Product added successfully'
            
        Product(name,price,quantity)
        return 'Product added successfully'
    
    def remove_from_menu(self,name):
        for product in self.menu:
            if product.name.lower() == name.lower():
                self.menu.remove(product)
                return 'Product successfully removed'
            
        return 'Item not found!'
        