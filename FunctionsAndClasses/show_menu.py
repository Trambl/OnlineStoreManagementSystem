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
    print("Products Menu:"\
        "\n\t1. View all products" \
        "\n\t2. Add new product"\
        "\n\t3. Update product information"\
        "\n\t4. Remove product"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")


def customers():
    print("Customers Menu:"\
        "\n\t1. View all customers"\
        "\n\t2. Add new customer"\
        "\n\t3. Update customer information"\
        "\n\t4. Remove customer"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")


def orders():
    print("Orders Menu:"\
        "\n\t1. View all orders"\
        "\n\t2. Place new order"\
        "\n\t3. Update order information"\
        "\n\t4. Remove order"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")

