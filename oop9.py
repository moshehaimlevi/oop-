import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def __repr__(self):
        return f"Point({self.__x}, {self.__y})"

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.__x == other.__x and self.__y == other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))


p1 = Point(3, 4)
p2 = Point(3, 4)


point_dict = {}
point_dict[p1] = math.sqrt(p1.get_x()**2 + p1.get_y()**2)
point_dict[p2] = "Point label"


for key, value in point_dict.items():
    print(f"{key}: {value}")











