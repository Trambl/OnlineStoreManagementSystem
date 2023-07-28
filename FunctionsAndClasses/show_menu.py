import re
import json


def is_valid_email(email):
    # Function to check if an email is valid using regex pattern matching.
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def write_json(file_path, data):
    # Function to write data to a JSON file with indentation.
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
            
            
def main_menu():
    # Function to display the main menu options.
    print("Main Menu:"\
        "\n\t1. Products"\
        "\n\t2. Customers"\
        "\n\t3. Orders"\
        "\n\t4. Exit")
    return input("Please choose between options 1-4: ")


def products():
    # Function to display the products menu options.
    print("Products Menu:"\
        "\n\t1. View all products" \
        "\n\t2. Add new product"\
        "\n\t3. Update product information"\
        "\n\t4. Remove product"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")


def customers():
    # Function to display the customers menu options.
    print("Customers Menu:"\
        "\n\t1. View all customers"\
        "\n\t2. Add new customer"\
        "\n\t3. Update customer information"\
        "\n\t4. Remove customer"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")


def orders():
    # Function to display the orders menu options.
    print("Orders Menu:"\
        "\n\t1. View all orders"\
        "\n\t2. Place new order"\
        "\n\t3. Update order information"\
        "\n\t4. Remove order"\
        "\n\t5. Return to Main Menu")
    return input("Please choose between options 1-5: ")
