class Figure:
    sides_count = 0

    def __init__(self, sides, color):
        self.__sides = sides
        self.__color = color
        self.filled = False

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and
                (isinstance(r, int) and isinstance(g, int) and isinstance(b, int))):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        for side in sides:
            if len(sides) == self.sides_count and isinstance(side, int) and side > 0:
                return True
            else:
                return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        side = 0
        for i in self.__sides:
            side += i
        return side

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1
    list_sides = []

    def __init__(self, color, long_side):
        self.__radius = long_side / (2 * 3.14)
        for i in range(self.sides_count):
            self.list_sides.append(long_side)
        super().__init__(color, self.list_sides)

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 0:
            self.set_sides(1, 1, 1)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__([sides] * 12, color)
        self.__sides = sides

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
