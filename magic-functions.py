
@author:Wahba

This script demonstrates the use of magic (or dunder) methods in Python. 
Magic methods start and end with double underscores and allow customization of 
class behavior during specific actions. They are invoked internally rather 
than being called directly. 
"""

# Class demonstrating magic methods
class Customer:
    """
    A class representing a Customer with a name and balance. 
    Includes magic methods for object initialization, string conversion, 
    comparison, and arithmetic operations.
    """
    
    def __init__(self, name, balance=5):  
        """
        Constructor to initialize Customer objects.
        Parameters:
            name (str): Name of the customer.
            balance (float): Initial balance of the customer (default: 5).
        """
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __str__(self):
        """Returns a user-friendly string representation of the Customer object."""
        return f'Customer: {self.name}, balance: {self.balance}'
    
    def __repr__(self):
        """Returns a developer-friendly string representation of the Customer object."""
        return f"Customer(name={self.name}, balance={self.balance})"
    
    # Magic methods for comparison
    def __eq__(self, other):
        """Checks equality of balance between two Customer objects."""
        return self.balance == other.balance
    
    def __lt__(self, other):
        """Checks if the balance is less than another Customer's balance."""
        return self.balance < other.balance
    
    def __le__(self, other):
        """Checks if the balance is less than or equal to another Customer's balance."""
        return self.balance <= other.balance
    
    def __gt__(self, other):
        """Checks if the balance is greater than another Customer's balance."""
        return self.balance > other.balance
    
    def __ge__(self, other):
        """Checks if the balance is greater than or equal to another Customer's balance."""
        return self.balance >= other.balance
    
    # Magic methods for arithmetic operations
    def __add__(self, other):
        """
        Adds the balances of two Customer objects and combines their names.
        Returns:
            Customer: A new Customer object with the combined name and balance.
        """
        return Customer(self.name + ' & ' + other.name, self.balance + other.balance)
    
    def __sub__(self, other):
        """
        Subtracts the balances of two Customer objects and combines their names.
        Returns:
            Customer: A new Customer object with the combined name and subtracted balance.
        """
        return Customer(self.name + ' & ' + other.name, self.balance - other.balance)

# Demonstrating magic methods
if __name__ == "__main__":
    # Creating Customer instances
    customer1 = Customer("Alice", 10)
    customer2 = Customer("Bob", 7)
    customer3 = Customer("Charlie", 10)

    # __str__ and __repr__ methods
    print(str(customer1))  # User-friendly string
    print(repr(customer2))  # Developer-friendly string

    # Comparison methods
    print(customer1 == customer3)  # Equality
    print(customer2 < customer1)   # Less than
    print(customer1 >= customer3)  # Greater than or equal to

    # Arithmetic methods
    customer4 = customer1 + customer2
    print(customer4)  # Combined Customer object

    customer5 = customer1 - customer2
    print(customer5)  # Subtracted Customer object

# Alternate implementation of arithmetic methods
class Customer:
    """
    Another example of a Customer class where arithmetic operations
    are performed with integers instead of another Customer object.
    """
    def __init__(self, name, balance=20):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __add__(self, other): 
        """Adds an integer to the balance and returns a new Customer object."""
        return Customer("Test_Customer", self.balance + other)

    def __sub__(self, other): 
        """Subtracts an integer from the balance and returns a new Customer object."""
        return Customer("Test_Customer", self.balance - other)

# Creating and manipulating Customer objects
c1 = Customer("Ali") 
c2 = c1 + 30
c3 = c1 - 3
print(c2.balance, c3.balance)  # Outputs: 50, 17

# Constructors vs. Destructors
class Employee:
    """
    Demonstrates the difference between constructors and destructors in Python.
    """
    def __init__(self, b=15):
        self.balance = b
        print('Employee created.')

    def __add__(self, other):
        """Subtracts a value from the balance and returns a new Employee object."""
        return Employee(self.balance - other)

    def __del__(self):
        """Destructor called when the object is deleted."""
        print('Destructor called, Employee deleted.')

# Creating and deleting Employee objects
obj1 = Employee()
obj2 = obj1 + 10
print(obj2.balance)  # Outputs: 5
del obj2  # Explicitly calls the destructor
