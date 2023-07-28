import json
import os
import pandas as pd
from FunctionsAndClasses.show_menu import write_json
from FunctionsAndClasses.customers import Customers
from FunctionsAndClasses.products import Products

"""
Users should be able to place new orders, specifying the customer and the products they want to purchase.
Users should be able to view all orders and their details.
Users should be able to update order information (e.g., add or remove products from an order).
Users should be able to process orders (mark them as shipped or completed).
"""

class Orders:
    @classmethod   
    def file_info(cls):
        file_path = os.path.join(os.path.dirname(__file__), "..", "Data", "orders.json")
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return file_path, data
    
    
    @classmethod            
    def view(cls):
        """Allows user to view current data in a json file"""
        _, data = cls.file_info()
        df = pd.DataFrame(data)
        print("-" * 50)
        if not df.empty:
            print(df)
        else:
            print("No orders in the DB right now")
    
    
    @classmethod       
    def add(cls):
        """Allows user to add data in a json file"""
        file_path, data = cls.file_info()
        
        if data:
            order_id = max(data, key=lambda x: x["order_id"])["order_id"] + 1
        else:
            order_id = 1
        
        _, customers_data = Customers.file_info()
        existing_customers = [customer["id"] for customer in customers_data]
        while True:
            try:
                customer_id = int(input("Please provide customer id: "))
            except ValueError:
                print("Customer id should be a number")
            if customer_id in existing_customers:
                break
            else:
                print(50 * "-")
                return print("ID doesn't exist in customers DB. Please add the customer prior to completing order for them.")
        
        products = []
        quantity = []
        _, products_data = Products.file_info()
        existing_products = [product["id"] for product in products_data]
        while True:
            try:
                product_id = input("Please provide product id, or press Enter if you've added all products: ")
                if not product_id:
                    break
                product_id = int(product_id)
            except ValueError:
                print("Product id should be a number")
            if product_id:
                if product_id in existing_products:
                    products.append(product_id)
                    while True:
                        try:
                            quantity.append(int(input("Please provide quantity: ")))
                            break
                        except ValueError:
                            print("Quantity should be a number")
                else:
                    print(50 * "-")
                    return print("ID doesn't exist in products DB. Please add the product prior to completing order for them.")
            else:
                break
            
    
        new_order = {"order_id": order_id, "customer_id": customer_id, "products": products, "quantity": quantity}
        data.append(new_order)
        write_json(file_path, data)
        print("-" * 50)
        print("Product added")
     
    """only this to finish"""
    @classmethod   
    def update(cls):
        """Allows user to update already existing json record"""
        file_path, data = cls.file_info()
        while True:
            try:
                id = int(input("Please specify order id to edit the order: "))
                break
            except ValueError:
                print("Order id should be a number")
        
        found = False
        
        for index, d in enumerate(data):
            if id == d["order_id"]:
                found = True
                index_to_update = index
                
        if found:
            while True:
                try:
                    customer_id = input("Update customer id (press Enter if you don't want to update it): ")
                    if customer_id:
                        customer_id = int(customer_id)
                    break
                except ValueError:
                    print("Customer id should be a number")
            
            _, products_data = Products.file_info()
            existing_products = [product["id"] for product in products_data]
            products = []
            quantity = [] 
            i = -1
            for product in data[index_to_update]['products']:
                i += 1
                try: 
                    product_id = input(f"Update product id ({product}) (press Enter if you don't want to update it): ")
                    if product_id:
                        product_id = int(product_id)
                        if product_id in existing_products:
                            products.append(product_id)
                        else:
                            print(50 * "-")
                            return print("ID doesn't exist in products DB. Please add the product prior to completing order for them.")
                    else:
                        products.append(product)
                except ValueError:
                    print("Product id should be a number")
                    continue
                
                while True:
                    try:
                        if not product_id:
                            quantity_value = input(f"Do you want to update quantity for product id ({product}): ")
                            if not quantity_value:
                                quantity.append(data[index_to_update]['quantity'][i])
                                break
                            quantity.append(int(quantity_value))
                        else:
                            quantity_value = input(f"Do you want to update quantity for new product id ({product_id}): ")
                            if not quantity_value:
                                quantity.append(data[index_to_update]['quantity'][i])
                                break
                            quantity.append(int(quantity_value))
                        break
                    except ValueError:
                        print("Quantity should be a number")
                
                
            while True:
                try: 
                    product_id = input("Do you want to add new product id to the order (press Enter if you don't want to add it): ")
                    if not product_id:
                        break
                    product_id = int(product_id)
                except ValueError:
                    print("Product id should be a number")
                    continue
                if product_id in existing_products:
                    products.append(product_id)
                else:
                    print(50 * "-")
                    return print("ID doesn't exist in products DB. Please add the product prior to completing order for them.")
                while True:
                    try:
                        quantity.append(int(input("Please provide quantity: ")))
                        break
                    except ValueError:
                        print("Quantity should be a number")
            
                
            
            data[index_to_update]["products"] = products   
            data[index_to_update]["quantity"] = quantity

            write_json(file_path, data)
            print("-" * 50)
            print("Information updated")
        else:
            print("-" * 50)
            print("Order not found")
        

    @classmethod   
    def remove(cls):
        """Allows user to remove already existing json record"""
        file_path, data = cls.file_info()
        
        while True:
            try:
                id = int(input("Please specify order id to be removed: "))
                break
            except ValueError:
                print("Order id should be a number")
        
        found = False
        
        for index, d in enumerate(data):
            if id == d["order_id"]:
                found = True
                index_to_remove = index
                
        if found:
            order = []
            order.append(data[index_to_remove])
            df = pd.DataFrame(order)
            print(df)
            while True:
                confirmation = input("Order above will be permanently removed. Last chance to cancel your action (press Enter to cancel or write 'y'/'yes' to confirm): ").lower()
                if confirmation == "y" or confirmation == "yes":
                    del data[index_to_remove]
                    print("-" * 50)
                    print("Order removed successfully")
                    write_json(file_path, data)
                    break
                elif not confirmation:
                    print("-" * 50)
                    print("Order won't be remvoed")
                    break
        else:
            print("-" * 50)
            print("Order not found")
            
"""
- Users should be able to place new orders, specifying the customer and the products they want to purchase.
- Users should be able to view all orders and their details.
- Users should be able to update order information (e.g., add or remove products from an order).
- Users should be able to process orders (mark them as shipped or completed).
"""