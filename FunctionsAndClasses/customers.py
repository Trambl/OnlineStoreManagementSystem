import json
import os
import pandas as pd
from menu_options import is_valid_email, write_json
    
class Customers:
    @classmethod
    def option(cls, option):
        global file_path
        file_path = os.path.join(os.path.dirname(__file__), "..", "Data", "customers.json")
        with open(file_path, "r") as json_file:
            global data
            data = json.load(json_file)   
        match option:  
            case 1:
                cls.view()
            case 2:
                while True:
                    name = input("Please provide customer name: ").title()
                    if not name:
                        continue
                    email = input("Please provide customer email address: ").lower()
                    if is_valid_email(email):
                        break
                    else:
                        print("Email is not valid.")
                cls.add(name, email)
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
            print("No customers in the DB right now")
            
    
    
    def add(name, email):
        """Allows user to add data in a json file"""
        if data:
            id = max(data, key=lambda x: x["id"])["id"] + 1
        else:
            id = 1
        new_customer = {"id": id, "name": name, "email": email}
        data.append(new_customer)
        write_json(file_path, data)
        print("-" * 50)
        print("User added")
        
        
        
    def update():
        """Allows user to update already existing json record"""
        while True:
            try:
                id = int(input("Please specify user id to edit the user: "))
                break
            except ValueError:
                print("User id should be a number")
        
        found = False
        
        for index, d in enumerate(data):
            if id == d["id"]:
                found = True
                index_to_update = index
                
        if found:
            name = input("Update name (press Enter if you don't want to update it): ").title()
            while True:
                email = input("Update email (press Enter if you don't want to update it): ").lower()
                if is_valid_email(email) or email == "":
                    break
                else:
                    print("Email is not valid.")
            if name:
                data[index_to_update]["name"] = name
            if email:
                data[index_to_update]["email"] = email
            write_json(file_path, data)
            print("-" * 50)
            print("Information updated")
        else:
            print("-" * 50)
            print("User not found")
        


    def remove():
        """Allows user to remove already existing json record"""
        
        while True:
            try:
                id = int(input("Please specify user id to be removed: "))
                break
            except ValueError:
                print("User id should be a number")
        
        found = False
        
        for index, d in enumerate(data):
            if id == d["id"]:
                found = True
                index_to_remove = index
                
        if found:
            customer = []
            customer.append(data[index_to_remove])
            df = pd.DataFrame(customer)
            print(df)
            while True:
                confirmation = input("Customer above will be permanently removed. Last chance to cancel your action (press Enter to cancel or write 'y'/'yes' to confirm): ").lower()
                if confirmation == "y" or confirmation == "yes":
                    del data[index_to_remove]
                    print("-" * 50)
                    print("Customer removed successfully")
                    write_json(file_path, data)
                    break
                elif not confirmation:
                    print("-" * 50)
                    print("Customer won't be remvoed")
                    break
        else:
            print("-" * 50)
            print("User not found")