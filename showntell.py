class Bank:
   def __init__(self, account_number, current_balance):
       self.account_number = account_number
       self.balance = current_balance
       self.transactions = []

def check_balance(self):
        print(self.balance)
def deposit(self, new_amount):
       self.balance += new_amount
       self.transactions.append(f"{new_amount} has been deposited to the account.")
       print(f"{new_amount} has been deposited in your account.")

def withdraw(self, new_amount):
        if new_amount <= self.balance:
            self.balance -= new_amount
            self.transactions.append(f"{new_amount} has been withdrawn.")
            return f"{new_amount} has been withdrawn successfully and the new balance is {self.balance}"
        else:
            print("Insufficient amount. Please top up.")
def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)


account = Bank(account_number="abcd123456789", current_balance=20000)

