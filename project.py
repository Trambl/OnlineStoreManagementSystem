import sys
import json
from menu_options import *
import customers as c

 
def main():
    print("Welcome to Management System!")
    while True:
        try:
            choice = int(main_menu())
            print("1st stage")
            while True:
                print("2nd stage")
                try:
                    match choice:
                        case 1:
                            option = int(products_menu())
                            print(choice)
                        case 2:
                            option = int(customers_menu())
                            c.Customers.option(option)
                        case 3:
                            option = int(orders_menu())
                        case 4:
                            sys.exit("Thank you for using our system. Have a great day!")
                        case _:
                            break
                except ValueError:
                    continue
        except ValueError:
            continue
        
        
    
if __name__ == "__main__":
    main()