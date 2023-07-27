import re
import json

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def write_json(file_path, data):
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            
def main_menu():
    print("Main Menu:"\
        "\n\t1. Products"\
        "\n\t2. Customers"\
        "\n\t3. Orders"\
        "\n\t4. Exit")
    return input("Please choose between options 1-4: ")


def products():
    # Users should be able to add new products with details like product name, price, and quantity in stock.
    # Users should be able to view all products and their details.
    # Users should be able to update product information (e.g., price or quantity).
    # Users should be able to remove products from the store.
    print("Products Menu:"\
        "\n\t1. View all products" \
        "\n\t2. Add new product"\
        "\n\t3. Update product information"\
        "\n\t4. Remove product"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")


def customers():
    """
    Users should be able to add new customers with details like name, email, and address.
    Users should be able to view all customers and their details.
    Users should be able to update customer information (e.g., email or address).
    Users should be able to remove customers from the store.
    """
    print("Customers Menu:"\
        "\n\t1. View all customers"\
        "\n\t2. Add new customer"\
        "\n\t3. Update customer information"\
        "\n\t4. Remove customer"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")


def orders():
    """
    Users should be able to place new orders, specifying the customer and the products they want to purchase.
    Users should be able to view all orders and their details.
    Users should be able to update order information (e.g., add or remove products from an order).
    Users should be able to process orders (mark them as shipped or completed).
    """
    print("Orders Menu:"\
        "\n\t1. View all orders"\
        "\n\t2. Place new order"\
        "\n\t3. Update order information"\
        "\n\t4. Change order status"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")

