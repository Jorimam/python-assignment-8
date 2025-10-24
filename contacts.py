"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"


def add_contact(data):
	print("name", data.get("name") )
	print("number", data.get("phone_number"))
	contact_book = contact_info
	print(f"{contact_book['name']} added")
	print(contact_book)
contact_info = {"name":"JO", "phone_number": 12345567}
add_contact(contact_info)

def contact(**kwargs):
	print(f"{kwargs['name']}")
	print(f"{kwargs['age']}")
	contact_book = {"name": kwargs['name'], "age": kwargs['age']}
	print(contact_book)
contact(name= "Jo", age = 12)
#contact(contact_info)
"""
contacts = {}

class Contact_book:
	def __init__(self, name, phone_number):
		self.name = name
		self.phone_number = phone_number
		contacts = {"name": name, "phone_number": phone_number}
		print(f"{name} added successfully")
		print(contacts)
	
	def delete_contact(self):
		print(f"{self.name} deleted")		
		print(contacts)
	
	def show_contacts(self):
		#contacts.update({"name": self.name, "phone number":self.phone_number})
		print(contacts)	
c1 = Contact_book("pip", 213)
c2 = Contact_book("jo", 123)

c1.show_contacts()
c2.delete_contact()
