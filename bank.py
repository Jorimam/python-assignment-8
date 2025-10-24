"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""

class Bank_account:
	def __init__(self, customer_name, balance):
		self.customer_name = customer_name
		self.balance = balance
		print(f"Account with name {customer_name} created successfully, with an opening balance of ${balance}")

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
		else:
			print("Deposit amount cannot be less than 0")


	def withdraw(self, amount):
		if amount <= 0:
			print("Withdrawal amount must be positive.")
			return False
		elif amount > self.balance:
			print("Insufficient balance.")
			return False
		else:
			self.balance -= amount
			print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
			return True

	def get_balance(self):
		return self.balance

acc = Bank_account("Bob", 1000)
acc.deposit(500)
acc.withdraw(200)
print(f" Your current balance is ${acc.get_balance()}")
