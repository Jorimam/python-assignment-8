"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""

class Cart:
    def __init__(self, ):
        self.cart = {}
        
    def add(self, item, quantity):
        self.item = item 
        self.quantity = quantity 
        self.cart.update({self.item:self.quantity})
        return self.cart 
    def remove(self, item):
        self.item = item 
        if self.item in self.cart:
            self.cart.pop(self.item)
            return "Removed"
        else:
            print(f"{self.item} not in cart")
            # return f"{self.item} not in cart"
    
    def show_cart(self):
        return self.cart
    
    def clear(self):
        self.cart.clear()

    def total_price(self,  price = {"Shoe":1000, "Shirt": 800}):
        
        total = 0
        for self.item in self.cart:
            if self.item in price:
                total += price[self.item] * self.quantity
                return total 
       
        


item = Cart()

item.add("Shoe", 5)
item.add("Shirt", 3)


print(item.show_cart())

print(item.total_price())
item.remove("Sho")
# print(item.show_cart())
# item.clear()
print(item.show_cart())

#TODO prices 