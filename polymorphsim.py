"""
Polymorphism in Python

Polymorphism means "many forms". In programming, it allows methods/functions/operators 
with the same name to behave differently based on the object or class they are acting upon.

This document illustrates polymorphism with examples such as operator overloading, 
function polymorphism, class polymorphism, and method overriding in inheritance.
"""

# Example 1: Polymorphism with the Addition Operator (Operator Overloading)
# The "+" operator behaves differently depending on the operand types.
num1 = 1
num2 = 2
print(num1 + num2)  # Adds numbers (Output: 3)

str1 = "Python"
str2 = "Programming"
print(str1 + " " + str2)  # Concatenates strings (Output: Python Programming)


# Example 2: Function Polymorphism in Python
# Functions like len() exhibit polymorphism by accepting different data types.
print(len("Programiz"))  # Length of a string (Output: 9)
print(len(["Python", "Java", "C"]))  # Length of a list (Output: 3)
print(len({"Name": "John", "Address": "Nepal"}))  # Length of a dictionary (Output: 2)


# Example 3: Class Polymorphism in Python
# Different classes can have methods with the same name, allowing polymorphic behavior.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

# Create instances of different classes
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# Demonstrate polymorphism by calling the same method on different objects
for vehicle in (car1, boat1, plane1):
    vehicle.move()


# Example 4: Polymorphism and Inheritance (Method Overriding)
# Child classes can override methods of the parent class to provide specific behavior.

from math import pi

class Shape:
    """Base class for shapes."""
    def __init__(self, name):
        self.name = name

    def area(self):
        """Method to calculate area, to be overridden by subclasses."""
        pass

    def __str__(self):
        return self.name

class Square(Shape):
    """Represents a square with a given side length."""
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        """Calculates the area of a square."""
        return self.length ** 2

class Circle(Shape):
    """Represents a circle with a given radius."""
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        """Calculates the area of a circle."""
        return pi * self.radius ** 2

# Create instances of different shapes
square = Square(4)
circle = Circle(7)

# Demonstrate polymorphism with overridden methods
print(square)  # Output: Square
print(f"Area of {square}: {square.area()}")  # Output: Area of Square: 16
print(circle)  # Output: Circle
print(f"Area of {circle}: {circle.area()}")  # Output: Area of Circle: 153.93804002589985
