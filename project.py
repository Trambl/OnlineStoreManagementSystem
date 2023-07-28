import sys
import FunctionsAndClasses.show_menu as show_menu
from FunctionsAndClasses.customers import Customers
from FunctionsAndClasses.products import Products
from FunctionsAndClasses.orders import Orders

# Mapping of user choices to corresponding functions in the show_menu, Customers, Products, and Orders classes.
ACTION_MAPPING = {
    (1, 1): Products.view,
    (1, 2): Products.add,
    (1, 3): Products.update,
    (1, 4): Products.remove,
    (2, 1): Customers.view,
    (2, 2): Customers.add,
    (2, 3): Customers.update,
    (2, 4): Customers.remove,
    (3, 1): Orders.view,
    (3, 2): Orders.add,
    (3, 3): Orders.update,
    (3, 4): Orders.remove,
}


def main():
    # Main function to start the Management System.
    print("Welcome to the Management System!")

    while True:
        # Display the main menu and get the user's choice.
        choice = show_menu.main_menu()
        status, choice = validate_input(choice, 1, 5)
        if not status:
            continue
        print(50 * "-")

        while True:
            # Process the user's choice for the submenu (Products, Customers, Orders).
            option = process_menu_choice(choice)
            status, option = validate_input(option, 1, 6)
            if not status:
                continue
            if not process_action(choice, option):
                break
            print(50 * "-")


def process_action(choice, option):
    # Execute the corresponding action based on the user's choice and option.
    action = ACTION_MAPPING.get((choice, option))
    if action:
        action()
        return True
    else:
        print(50 * "-")
        return False


def process_menu_choice(choice):
    # Map the main menu choice to the appropriate submenu (Products, Customers, Orders).
    match choice:
        case 1:
            return show_menu.products()
        case 2:
            return show_menu.customers()
        case 3:
            return show_menu.orders()
        case 4:
            sys.exit("Thank you for using our system. Have a great day!\n" f"{50 * '-'}")


def validate_input(choice, x, y):
    # Validate if the user's choice is within the specified range (x, y).
    try:
        choice = int(choice)
        if choice not in range(x, y):
            raise ValueError
        return True, choice
    except ValueError:
        error_message()
        return False, choice


def error_message():
    # Display an error message when the user provides an invalid input.
    print(
        f"{50 * '-'}"
        "\nPlease choose from available options. Keep in mind that choice should be a number."
        f"\n{50 * '-'}"
    )


if __name__ == "__main__":
    main()
