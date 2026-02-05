import json
import os
filename = "inventory.json"
def load():
    if not os.path.exists(filename):
        return{}
    with open(filename,"r") as file:
        return json.load(file)
def save(Inventory):
        with open(filename,"w") as file:
            json.dump (Inventory,file,indent=4)
def add (Inventory,Name,Qty,Price):
    Inventory[Name] = {"Qty":Qty,"Price":Price}
def updateqty (Inventory,Name,Qty):
    if(Name in Inventory):
        Inventory[Name]["Qty"]=Qty
    else:
        print(f"{Name} is not found in Inventory")
Inventory = load()
add(Inventory, "Laptop", 10, 9876)
add(Inventory,"Mouse", 9, 567)
updateqty(Inventory,'Product1',97)
save(Inventory)
print("Inventory Updated")