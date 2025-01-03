import os

ACCOUNT_NUMBER = "account_number"
NAME = "name"
BALANCE = "balance"
FILE_NAME = "accounts.txt"

class Account:
    def __init__(self, account_number, name, balance = 0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Balance is less than withdrawal amount")
        
        self.balance -= amount
    
    def to_string(self):
        return f"{self.account_number},{self.name},{self.balance}"
    
    @staticmethod
    def from_string(data):
        account_number, name, balance = data.strip().split(",")
        return Account(account_number, name, balance)

class Bank:
    file_name = FILE_NAME

    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = str(1) if len(self.accounts) == 0 else str(sorted(self.accounts.keys())[-1] + 1)
        
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be greater than or equal 0")
        
        account = Account(account_number, name, initial_deposit)
        self.accounts[account.account_number] = account
        self.save_to_file()

        print(f"Account created successfully! Account Number: {account_number}")
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)

        if not account:
            raise ValueError("Account not found")
    
        print(f"Account Number: {account.account_number}, Name: {account.name}, Balance: ${account.balance}")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)

        if not account:
            raise ValueError("Account not found")
        
        account.deposit(amount)
        self.save_to_file()

        print(f"Deposit successful! New Balance: ${account.balance}")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)

        if not account:
            raise ValueError("Account not found")
        
        account.withdraw(amount)
        self.save_to_file()

        print(f"Withdrawal successful! New Balance: ${account.balance}")

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            for account in self.accounts.values():
                file.write(account.to_string() + "\n")

    def load_from_file(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as file:
                pass
        
        with open(self.file_name, "r") as file: 
            for line in file:
                if line.strip():
                    account = Account.from_string(line)
                    self.accounts[account.account_number] = account
        
bank = Bank()

while True:
    print("\nBank Application")
    print("1. Create an account")
    print("2. View account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)
        elif choice == 2:
            account_number = input("Enter account number: ")
            bank.view_account(account_number)
        elif choice == 3:
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == 4:
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == 5:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error: {e}")
            