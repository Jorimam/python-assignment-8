"""
TASK: Create an Inventory class.

Requirements:
1. Store items in a dictionary (item_name → quantity).
2. Provide a method to add items (with quantity).
3. Provide a method to remove items (only if available).
4. Provide a method to update stock levels.
5. Provide a method to display all inventory items.

Example Usage:
    treasure_store = Inventory()
    favour_store = Inventory()

    treasure_store.add_item("Apples", 50)
    treasure_store.add_item("Bananas", 30)
    treasure_store.remove_item("Apples", 10)
    print(treasure_store.show_inventory())  # {"Apples": 40, "Bananas": 30}

    favour_store.add_item("Milk", 50)
    favour_store.add_item("Garri", 30)
    favour_store.remove_item("Milk", 40)
    print(treasure_store.show_inventory())  # {"Milk": 10, "Garri": 30}
"""
class Inventory:
    def __init__(self):
        self.store = {}
    def add(self, item_name, quantity):
        self.item_name = item_name 
        self.quantity = quantity
        if self.item_name in self.store:
            print(f"{self.item_name} already in store")
        else:
            self.store.update({self.item_name:quantity})

    def show(self):
        return self.store
    def remove(self, item_name):
        self.item_name = item_name
        if self.item_name in self.store:
            self.store.pop(self.item_name)
            print(f"{self.item_name} removed")
        else:
            
            print(f"{self.item_name} not in store")
    def change(self, item, new_quantity):
        self.item = item
        self.new_quantity = new_quantity
        if self.item in self.store:
            self.store[self.item] = new_quantity
        else:
            print(f"{self.item_name} not in store")
        

chima = Inventory()
gold = Inventory()

chima.add("Shoe", 12)
chima.add("Tv", 20)
gold.add("Shirt", 1000)
gold.add("Bed", 10)

gold.change("Shirt", 510)

chima.remove("Shoe")
gold.remove("crown")

print(chima.show())
print(gold.show())
