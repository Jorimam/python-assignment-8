"""
TASK: Create a RestaurantOrder class.

Requirements:
1. Store orders in a dictionary (item → quantity).
2. Provide a method to add items to the order.
3. Provide a method to remove items from the order.
4. Provide a method to calculate the total bill (use a price list dictionary).
5. Provide a method to show the current order.

Example Usage:
    prices = {"Pizza": 2000, "Burger": 1500, "Drink": 500}
    order = RestaurantOrder(prices)
    order.add_item("Pizza", 2)
    order.add_item("Drink", 3)
    print(order.calculate_total())  # 5500
"""
class RestuarantOrder:
    def __init__(self):
        self.order = {}
       
    def add(self, item, quantity):
        self.item = item
        self.quantity = quantity
        if self.item not in self.order:
            self.order.update({self.item:self.quantity})
            
        else:
            print(f"You have alaeady ordered {self.item}")
    def remove(self, item):
        self.item = item 
        if self.item in self.order:
            self.order.pop(self.item)
        else:
            print(f"{self.item} not found")
    def calculate_total(self):
        total = 0
        prices = {"Bag": 2000, "Burger": 1500, "Drink": 500}
        for item in self.order:
            if item in prices:
                total += (self.order[self.item] * prices[item])
        print(total)
    def show_order(self):
        return self.order
    

order = RestuarantOrder()
order.add("Bag", 2 )
order.add("Burger", 5)

# order.remove("Bag")
order.calculate_total()
print(order.show_order())