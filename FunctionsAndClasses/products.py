import json
import os
import pandas as pd
from menu_options import write_json

class Products:
    @classmethod
    def option(cls, option):
        global file_path
        file_path = os.path.join(os.path.dirname(__file__), "..", "Data", "products.json")
        with open(file_path, "r") as json_file:
            global data
            data = json.load(json_file)   
        match option:  
            case 1:
                cls.view()
            case 2:
                while True:
                    name = input("Please provide Product name: ").title()
                    if not name:
                        continue
                    
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
                    break
                            
                cls.add(name, price, quantity)
            case 3:
                cls.update()
            case 4:
                cls.remove()
            case 5:
                return True
                
    def view():
        """Allows user to view current data in a json file"""
        df = pd.DataFrame(data)
        print("-" * 50)
        if not df.empty:
            print(df)
        else:
            print("No products in the DB right now")
            
    def add(name, price, quantity):
        """Allows user to add data in a json file"""
        if data:
            id = max(data, key=lambda x: x["id"])["id"] + 1
        else:
            id = 1
        total_price = quantity * price
        
        price = "{:,.2f}".format(price)
        quantity = "{:,.2f}".format(quantity)
        total_price = "{:,.2f}".format(total_price)
    
        new_product = {"id": id, "name": name, "quantity": quantity, "price": price, "total price": total_price}
        data.append(new_product)
        write_json(file_path, data)
        print("-" * 50)
        print("Product added")
        
    def update():
        """Allows user to update already existing json record"""
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
        


    def remove():
        """Allows user to remove already existing json record"""
        
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