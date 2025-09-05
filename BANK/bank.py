# bank.py
from customer import Customer
from employee import Employee, Teller, Manager

class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []      # list of branch names
        self.customers = []     # list of Customer objects
        self.employees = []     # list of Employee objects

    def add_branch(self, branch_name):
        self.branches.append(branch_name)
        print(f"Branch '{branch_name}' added to {self.name} Bank.")

    def add_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} added to {self.name} Bank.")

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} ({employee.position}) added to {self.name} Bank.")

    def list_customers(self):
        print(f"=== Customers of {self.name} Bank ===")
        if not self.customers:
            print("No customers found.")
        for c in self.customers:
            print(f"- {c}")

    def list_employees(self):
        print(f"=== Employees of {self.name} Bank ===")
        if not self.employees:
            print("No employees found.")
        for e in self.employees:
            print(f"- {e}")

    def __str__(self):
        return f"Bank: {self.name} | Branches: {len(self.branches)} | Customers: {len(self.customers)} | Employees: {len(self.employees)}"
