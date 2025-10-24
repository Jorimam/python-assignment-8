"""
TASK: Create a Bus class.

Requirements:
1. Store bus capacity and passenger list.
2. Provide a method to add a passenger (if space available).
3. Provide a method to remove a passenger.
4. Provide a method to show all passengers.

Example Usage:
    metro_bus = Bus(capacity=3)
    metro_bus.add_passenger("John")
    metro_bus.add_passenger("Mary")
    metro_bus.add_passenger("Paul")
    metro_bus.add_passenger("Lisa")  # "Bus is full!"
    print(bus.show_passengers())  # ["John", "Mary", "Paul"]
"""
class Bus():
    def __init__(self, capacity):
        self.bus = []
        self.capacity = capacity
    def add(self, passenger_name):
        self.name = passenger_name
        if self.capacity > len(self.bus):
            self.bus.append(self.name)
            
        else:
            print(f"{self.bus} is full")
    def remove(self, passenger_name):
        self.name = passenger_name
        if self.name in self.bus:
            self.bus.remove(self.name)
        else:
            print(f"{self.name} not in {self.bus}")
    def show_passengers(self):
        return self.bus

metro = Bus(2)
metro.add("Jo")
metro.add("Jon")
metro.remove("Jo")
metro.add("Joe")
print(metro.show_passengers())
