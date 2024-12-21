from users import Customer, Admin
from restaurant import Restaurant





# Restaurant Details


restaurant = Restaurant('Khabar Dabar','Cumilla')
ad = Admin('Admin','admin@gmail.com')





while True:
    print('\n--- Restaurant Management System ---')
    print('')
    print('1. Admin Login')
    print('2. Customer Login')
    print('3. Exit')
    option = int(input('Select an option : '))
    
    if option == 1:
        admin = input('Enter Admin name : ')
        if admin == 'Admin':
            while True: 
                print(f'\n--- {admin} Menu ---')
                print('')
                print('1. Create Customer Account')
                print('2. Remove Customer Account')
                print('3. View All Customers')
                print('4. Manage Restaurant Menu')
                print('5. Exit')
                choice = int(input('Select an option : '))
                if choice == 1:
                    # create customer account
                    name = input('Enter name : ')
                    email = input('Enter email : ')
                    address = input('Enter address : ')
                    balance = int(input('Enter first deposit : '))
                    ad.add_customer(name,email,address,balance)
                    
                elif choice == 2:
                    # remove account
                    email = input('Enter email for removing a customer : ')
                    ad.remove_customer(email)
                    
                elif choice == 3:
                    # show customers
                    ad.view_customer_list()
                    
                elif choice == 4:
                    # restaurant menu
                    while True:
                        restaurant.view_menu()
                        print('\n')
                        print('1. Add Item')
                        print('2. Remove Item')
                        print('3. Update Price')
                        print('4. Exit')
                        chose = int(input('Select an option : '))
                        if chose == 1:
                            name = input("Enter product name : ")
                            price = int(input('Enter price : '))
                            quantity = int(input('Enter products\'s quantity : '))
                            restaurant.add_to_menu(name,price,quantity)
                        elif chose == 2:
                            name = input('Enter name for removing Item : ')
                            restaurant.remove_from_menu(name)
                        elif chose == 3:
                            name = input('Enter product name : ')
                            price = int(input('Enter updated price : '))
                            ad.update_price(name,price)
                        elif chose == 4:
                            break
                        else:
                            print('Selected wrong option. Try again!')
                        
                elif choice == 5:
                    break
                else:
                    print('Selected a wrong option. Try again!')
                    
        else:
            print('Entered wrong Admin name!')
    
    
    elif option == 2:
        cust = input('Enter Customer Username : ')
        found = False
        customer = None
        for i in Customer.customers:
            if i.name == cust:
                found = True
                customer = i
                break
        if found :
            while True:
                print(f'\n--- {cust} Menu ---')
                print('')
                print('1. View Restaurant Menu')
                print('2. View Balance')
                print('3. Add Balance')
                print('4. Place Order') 
                print('5. View Past Orders')
                print('6. Exit')
                
                op = int(input('Select an option : '))
                
                if op == 1:
                    # view menu
                    restaurant.view_menu()
                elif op == 2:
                    #view balace
                    print(f'\nRemaining Balance{customer.check_balance()}')
                elif op == 3:
                    # add balance
                    amount = int(input('Enter amount'))
                    customer.add_funds(amount)
                elif op == 4:
                    # place order
                    restaurant.view_menu()
                    name = input('Enter Item\'s Name : ')
                    quantity = int(input('Enter quantity : '))
                    customer.place_order(name,quantity)
                elif op == 5:
                    # view past order
                    customer.view_past_order()
                elif op == 6:
                    break
                else:
                    print('Selected a wrong option. Try again!')
                    
    elif option == 3:
        break
    else:
        print('Selected a wrong option. Try again!')