class Point():
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x

    def __repr__(self):
        return "(" + str(self.get_x()) + ',' + str(self.get_y()) + ')'


class Figure():
    def __init__ (self, points=[]):
        self.points = points

    def get_points(self):
        return self.points

    def __repr__(self):
        return str(self.get_points())

    def is_in(self, point): #метод подразумевает работу только с треугольниками
        xp = point.get_x()
        xy = point.get_y()
        q = (self.points[0].get_x() - xp) * (self.points[1].get_y()-self.points[0].get_y()) - (self.points[1].get_x() - self.points[0].get_x()) * (self.points[0].get_y() - xy)
        w = (self.points[1].get_x() - xp) * (self.points[2].get_y()-self.points[1].get_y()) - (self.points[2].get_x() - self.points[1].get_x()) * (self.points[1].get_y() - xy)
        p = (self.points[2].get_x() - xp) * (self.points[0].get_y()-self.points[2].get_y()) - (self.points[0].get_x() - self.points[2].get_x()) * (self.points[2].get_y() - xy)
        if (q >= 0) and (w>=0) and (p>=0):
            return "in"
        else:
            return "out"

a = Point(1, 3)
b = Point(5, 6)
c = Point(-5, 2)


fig = Figure([a, b, c])

print(fig)
d = Point (7,6) #тут может быть любая точка, я просто сделала ввод из кода, а не с консоли
print(fig.is_in(d))


