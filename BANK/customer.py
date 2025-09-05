"""
The Customer class represents a bank customer. 
It stores personal details (ID, name, address, phone) and manages 
the customer’s accounts. It provides methods to open and close accounts, 
retrieve a list of account numbers, and display customer information.
"""

class Customer:
    def __init__(self, customer_id, name, address, phone):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.accounts = []

    def open_account(self, account):
        """Add a new account to the customer"""
        self.accounts.append(account)
        print(f"Account {account.account_number} opened for {self.name}")

    def close_account(self, account_number):
        """Close an account by account number"""
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} closed for {self.name}")
                return
        print(f"Account {account_number} not found for {self.name}")

    def get_accounts(self):
        """Return list of account numbers"""
        return [account.account_number for account in self.accounts]

    def __str__(self):
        return f"Customer[{self.customer_id}] - {self.name}"
