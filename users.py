from products import Product
from orders import Order
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    
    
class Customer(User):
    customers = []
    
    def __init__(self, name, email,balance,address):
        super().__init__(name, email)
        self.__balance = balance
        self.address = address
        self.orders = []
        Customer.customers.append(self)
        
        
        
    def check_balance(self):
        return f'{self.__balance}'
    
    def add_funds(self,amount):
        self.__balance += amount
        
        print(f'{amount}Tk added to your account. Your current balance is {self.__balance}Tk.')
    
    def place_order(self,name,quantity):
        found_product = False
        print('Placing order..........')
        for product in Product.products:
            if product.name.lower() == name.lower():
                found_product = True
                if product.quantity < quantity:
                    print('Not enough quantity available')
                    return
                if product.price * quantity > self.__balance:
                    print('Not enough money in your account')
                    return
                break
        if not found_product:
            print('Product not found')
            return
        
        
        order = Order(name,quantity)
        self.orders.append(order)
        self.__balance -= order.total
        print(f'Order placed succesfully remaining balance {self.__balance}Tk.')
    
    def view_past_order(self):
        print('Past orders:')
        print('-----------------Ordered Item-----------------')
        print('Name\t Quantity\t Total')
        total = 0
        for order in self.orders:
            print(f'{order.name}\t    {order.quantity}\t\t {order.total}')
            total += order.total
        print(f'\n\n\t\t\t Total {total}')
    
    
    

class Admin(User):
    def __init__(self, name,email):
        super().__init__(name,email)
        
    # Manage Restaurrent Menu
    def add_products(self,name,price,quantity):
        for product in Product.products:
            if product.name.lower() == name.lower():
                product.quantity += quantity
        else:
            Product(name,price,quantity)
            return 'Product added successfully!'
            
    def remove_products(self,name):
        for product in Product.products:
            if product.name == name:
                Product.products.remove(product)
                break
        else:
            print('Entered wrong name')
            
    def update_price(self,name,price):
        for product in Product.products:
            if product.name == name:
                product.update_price(price)
    
    def view_customer_list(self):
        print('Name\t Email\t Cur Balance')
        for customer in Customer.customers:
            print(f'{customer.name}\t {customer.email}\t {customer.check_balance()}')
            
    def add_customer(self,name,email,address,balance):
        Customer(name,email,balance,address)
        print(f'Customer {name} added successfully!')
            
    def remove_customer(self,email):
        for customer in Customer.customers:
            if customer.email == email:
                print(f'Customer {customer.name} Removed')
                Customer.customers.remove(customer)
                break
            
        else:
            print(f'No customer found with email {email}')
        
    
    