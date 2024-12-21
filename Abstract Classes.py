# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:50:56 2023

@author: Wahba

This script demonstrates the concept of abstract classes in Python using the ABC module.
Abstract classes act as a blueprint for other classes, requiring derived classes to implement 
specific methods. This example defines a Polygon abstract class and its concrete implementations.
"""

# Importing the ABC module for creating abstract base classes
from abc import ABC, abstractmethod 

# Define the abstract base class
class Polygon(ABC): 
    """
    Polygon is an abstract base class that serves as a template for different types of polygons.
    Derived classes must implement the noofsides method.
    """
    @abstractmethod
    def noofsides(self): 
        """
        Abstract method to define the number of sides of a polygon.
        Must be implemented by all subclasses.
        """
        pass

# Define a concrete class for triangles
class Triangle(Polygon): 
    """
    Represents a triangle with three sides.
    """
    def noofsides(self): 
        # Implementation of the abstract method
        print("I have 3 sides") 

# Define a concrete class for pentagons
class Pentagon(Polygon): 
    """
    Represents a pentagon with five sides.
    """
    def noofsides(self): 
        # Implementation of the abstract method
        print("I have 5 sides") 

# Define a concrete class for hexagons
class Hexagon(Polygon): 
    """
    Represents a hexagon with six sides.
    """
    def noofsides(self): 
        # Implementation of the abstract method
        print("I have 6 sides") 

# Define a concrete class for quadrilaterals
class Quadrilateral(Polygon): 
    """
    Represents a quadrilateral with four sides.
    """
    def noofsides(self): 
        # Implementation of the abstract method
        print("I have 4 sides") 

# Driver code to demonstrate polymorphism with abstract classes
if __name__ == "__main__":
    # Create instances of each subclass and call their noofsides method
    R = Triangle() 
    R.noofsides()  # Output: I have 3 sides

    K = Quadrilateral() 
    K.noofsides()  # Output: I have 4 sides

    R = Pentagon() 
    R.noofsides()  # Output: I have 5 sides

    K = Hexagon() 
    K.noofsides()  # Output: I have 6 sides
