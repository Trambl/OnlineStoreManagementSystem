import json
import os
import pandas as pd
from show_menu import write_json


class Products:
    @classmethod   
    def file_info(cls):
        file_path = os.path.join(os.path.dirname(__file__), "..", "Data", "products.json")
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
            print("No products in the DB right now")
    
    
    @classmethod       
    def add(cls):
        """Allows user to add data in a json file"""
        file_path, data = cls.file_info()
        
        if data:
            id = max(data, key=lambda x: x["id"])["id"] + 1
        else:
            id = 1
        
        while True:
            name = input("Please provide product name: ").title()
            if name:
                break  
            
        while True:
            try: 
                price = round(float(input("Please provide product price: ")), 2)
                break
            except ValueError:
                print("Price should be a number.")
                continue  
            
        while True:
            try: 
                quantity = round(float(input("Please provide product quantity: ")),2)
                break
            except ValueError:
                print("Quantity should be a number.")
                continue
            
        total_price = quantity * price
        
        price = "{:,.2f}".format(price)
        quantity = "{:,.2f}".format(quantity)
        total_price = "{:,.2f}".format(total_price)
    
        new_product = {"id": id, "name": name, "quantity": quantity, "price": price, "total price": total_price}
        data.append(new_product)
        write_json(file_path, data)
        print("-" * 50)
        print("Product added")
     
     
    @classmethod   
    def update(cls):
        """Allows user to update already existing json record"""
        file_path, data = cls.file_info()
        while True:
            try:
                id = int(input("Please specify product id to edit the product: "))
                break
            except ValueError:
                print("Product id should be a number")
        
        found = False
        
        for index, d in enumerate(data):
            if id == d["id"]:
                found = True
                index_to_update = index
                
        if found:
            
            name = input("Update name (press Enter if you don't want to update it): ").title()
                
            while True:
                try: 
                    price = input("Update price (press Enter if you don't want to update it): ")
                    price = round(float(price), 2)
                    break
                except ValueError:
                    
                    print("Price should be a number")
                    continue
              
            
            while True:
                try: 
                    quantity = input("Update quantity (press Enter if you don't want to update it): ")
                    quantity = round(float(quantity), 2)
                    break
                except ValueError:
                    if quantity == "":
                        break
                    print("Quantity should be a number")
                    continue
                
            if name:
                data[index_to_update]["name"] = name   
            if price:
                price = "{:,.2f}".format(price)
                data[index_to_update]["price"] = price
            if quantity:
                quantity = "{:,.2f}".format(quantity)
                data[index_to_update]["quantity"] = quantity
            if price or quantity:
                total_price = float(data[index_to_update]["price"].replace(",","")) * float(data[index_to_update]["quantity"].replace(",",""))
                total_price = "{:,.2f}".format(total_price)
                data[index_to_update]["total price"] = total_price
                
            write_json(file_path, data)
            print("-" * 50)
            print("Information updated")
        else:
            print("-" * 50)
            print("Product not found")
        

    @classmethod   
    def remove(cls):
        """Allows user to remove already existing json record"""
        file_path, data = cls.file_info()
        
        while True:
            try:
                id = int(input("Please specify product id to be removed: "))
                break
            except ValueError:
                print("Product id should be a number")
        
        found = False
        
        for index, d in enumerate(data):
            if id == d["id"]:
                found = True
                index_to_remove = index
                
        if found:
            product = []
            product.append(data[index_to_remove])
            df = pd.DataFrame(product)
            print(df)
            while True:
                confirmation = input("Product above will be permanently removed. Last chance to cancel your action (press Enter to cancel or write 'y'/'yes' to confirm): ").lower()
                if confirmation == "y" or confirmation == "yes":
                    del data[index_to_remove]
                    print("-" * 50)
                    print("Product removed successfully")
                    write_json(file_path, data)
                    break
                elif not confirmation:
                    print("-" * 50)
                    print("Product won't be remvoed")
                    break
        else:
            print("-" * 50)
            print("Product not found")