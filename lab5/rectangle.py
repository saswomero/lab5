class Colour():
    def __init__(self, colour):
        self.colour = colour

    def get_col(self):
        return self.colour


class Rectangle():
    def __init__(self, height, width):
        a = Colour("purple")
        self.colour = a.get_col()
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return ("Colour: " + str(self.colour) + '\n' + "Width: " + str(self.width) + '\n' + "Height: " + str(self.height) + '\n' +"Square: "+ str(self.square()))


class Square (Rectangle):
    def __init__(self, l):
        a = Colour("purple")
        self.colour = a.get_col()
        self.l = l
        self.height = l
        self.width = l


