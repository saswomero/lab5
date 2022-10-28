from math import*

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return pi*self.radius

    def __repr__(self):
        return ("Radius: " + str(self.radius) + '\n' + "Square: " + str(self.square()))

