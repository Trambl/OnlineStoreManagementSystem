import json
import os
import pandas as pd
from menu_options import is_valid_email, write_json
    
class Customers:
    @classmethod
    def option(self, option):
        global file_path
        file_path = os.path.join(os.path.dirname(__file__), "..", "Data", "customers.json")
        with open(file_path, "r") as json_file:
            global data
            data = json.load(json_file)   
        match option:  
            case 1:
                self.view()
            case 2:
                name = input("Please provide customer name: ")
                while True:
                    email = input("Please provide customer email address: ")
                    if is_valid_email(email):
                        break
                    else:
                        print("Email is not valid.")
                self.add(name, email)
            case 3:
                self.update()
            case 4:
                self.remove()
            case 5:
                return True
                
                
    # Users should be able to add new products with details like product name, price, and quantity in stock.
    # Users should be able to view all products and their details.
    # Users should be able to update product information (e.g., price or quantity).
    # Users should be able to remove products from the store.
            
    def view():
        """Allows user to view current data in a json file"""
        print(data)
        df = pd.DataFrame(data)
        print(df)
    
    def add(name, email):
        """Allows user to add data in a json file"""
        id = max(data, key=lambda x: x["id"])["id"] + 1
        new_customer = {"id": id, "name": name, "email": email}
        data.append(new_customer)
        write_json(file_path, data)
        
    def update():
        """Allows user to update already existing json record"""
        ...
        
    def remove():
        """Allows user to remove already existing json record"""
        ...
        
    