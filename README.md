# OnlineStoreManagementSystem

Command-line-based online store management system that allows users to manage products, customers, and orders for an online store. The application provides functionalities for adding, viewing, updating, and deleting products and customers, as well as placing and processing orders.

## Description

This Online Store Management System is a command-line application built to help store administrators efficiently manage their online store's products, customers, and orders. The system provides various functionalities to perform CRUD operations on products and customers, as well as handle orders, such as placing new orders, viewing existing orders, updating order information, and processing orders (e.g., marking them as shipped or completed).

The management system is composed of the following modules:

1. `project.py`: The main script that serves as the entry point for the application. It presents the main menu and submenus to the user and calls relevant functions based on the user's input.

2. `show_menu.py`: Contains functions to display the various menus to the user, such as the main menu, product menu, customer menu, and order menu. It also includes helper functions for validating user input.

3. `customers.py`: Provides functionalities related to managing customer data. It allows users to view all customers, add new customers, update customer information, and remove customers from the system.

4. `products.py`: Handles the management of product data. Users can view all products, add new products, update product information, and remove products using this module.

5. `orders.py`: Handles the management of order data. Users can view all orders, place new orders specifying customers and products, update existing orders (e.g., add or remove products), and remove orders.

## Getting Started

1. Clone the repository to your local machine:

```
git clone https://github.com/yourusername/OnlineStoreManagementSystem.git
cd OnlineStoreManagementSystem
```

2. Ensure you have Python 3.x installed on your system.

3. Install the required dependencies:

```
pip install pandas
```

4. Run the main script to start the Online Store Management System:

```
python project.py
```

## How to Use

1. When you run the main script, the Management System will greet you with the main menu, where you can choose between managing products, customers, or orders.

2. Select the desired option from the main menu (1-3) to proceed to the respective submenu.

3. In the submenu, you can choose from various options (1-5) to perform specific tasks related to products, customers, or orders.

4. Follow the instructions provided in the command-line interface to add, view, update, or remove data as needed.

5. When you are finished, you can exit the system by selecting option 4 from the main menu.

## Examples

1. Adding a new product:

```
Please provide product name: Laptop
Please provide product price: 999.99
Please provide product quantity: 50
Product added
```

2. Placing a new order:

```
Please provide customer id: 101
Please provide product id, or press Enter if you've added all products: 1
Please provide quantity: 2
Do you want to add new product id to the order (press Enter if you don't want to add it): 2
Please provide quantity: 3
Product added
```

3. Viewing all customers:

```
--------------------------------------------------
   id       name              email
0   1    John Doe      john@example.com
1   2  Jane Smith     jane.smith@example.com
2   3   Bob Brown       bbrown@example.com
--------------------------------------------------
```

## License

This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).

## Acknowledgments

This Online Store Management System is a demonstration project and not intended for production use. It was created as an educational exercise to showcase Python programming and command-line application development skills.

Contributions to the project are welcome! Please feel free to submit any issues or pull requests.