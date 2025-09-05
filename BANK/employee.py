"""
This module defines the Employee hierarchy for a banking system.

- Employee: Base class that represents a generic bank employee, 
  storing employee details and providing a method to assist customers.

- Teller: Subclass of Employee specialized in handling basic customer 
  transactions.

- Manager: Subclass of Employee with higher-level responsibilities, 
  such as handling important customer issues and approving/rejecting loans.
"""

class Employee:
    """
    Represents a bank employee with an ID, name, and position.
    Provides basic customer assistance functionality.
    """
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position

    def assist_customer(self, customer):
        """Basic assistance to a customer"""
        print(f"Employee {self.name} is assisting customer {customer.name}")

    def __str__(self):
        return f"Employee[{self.employee_id}] - {self.name} ({self.position})"


class Teller(Employee):
    """
    A Teller is an Employee who handles transactions 
    and provides customer-facing services at the bank counter.
    """
    def __init__(self, employee_id, name):
        super().__init__(employee_id, name, position="Teller")

    def assist_customer(self, customer):
        """Teller-specific assistance"""
        print(f"Teller {self.name} is handling transactions for customer {customer.name}")


class Manager(Employee):
    """
    A Manager is an Employee who handles more critical customer interactions 
    and has the authority to approve or reject loan applications.
    """
    def __init__(self, employee_id, name):
        super().__init__(employee_id, name, position="Manager")

    def assist_customer(self, customer):
        """Manager-specific assistance"""
        print(f"Manager {self.name} is meeting customer {customer.name} for important issues")

    def approve_loan(self, loan_amount):
        """
        Approve or reject a loan based on a simple rule.
        Loans up to 50,000 are approved, others are rejected.
        """
        if loan_amount <= 50000:
            print(f"Manager {self.name} approved loan of {loan_amount}")
        else:
            print(f"Manager {self.name} rejected loan of {loan_amount}")
