class Employees:
    def __init__(self):
       self.db = {}
    def add(self, name):
         self.name = name
         self.db.update({self.name:[]})
         return self.db 
    def remove(self,name):
      self.name = name 
      if self.name in self.db:
          self.db.pop(self.name)
    def show(self):
        return self.db 
 

e1 = Employees()
e1.add("Harry")
e1.add("manny")

print(e1.show())
e1.remove("Harry")
print(e1.show())
names = {"name": "Bob", "age": 12}
print(names)