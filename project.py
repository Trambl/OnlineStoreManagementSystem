import sys
import json
sys.path.append("FunctionsAndClasses")

from menu_options import *
import customers as c
import products as p
import orders as o

def main():
    print("Welcome to Management System!")
    while True:
        try:
            choice = int(main_menu())
            while True:
                try:
                    match choice:
                        case 1:
                            option = int(products_menu())
                            if p.Products.option(option):
                                break # Exit the inner loop and return to the main menu
                        case 2:
                            option = int(customers_menu())
                            if c.Customers.option(option):
                                break  # Exit the inner loop and return to the main menu
                        case 3:
                            option = int(orders_menu())
                            break  # Exit the inner loop and return to the main menu
                        case 4:
                            sys.exit("Thank you for using our system. Have a great day!")
                        case _:
                            break  # Exit the inner loop and return to the main menu
                except ValueError:
                    continue
        except ValueError:
            continue

if __name__ == "__main__":
    main()
