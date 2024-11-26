class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __eq__(self, other):  # 1
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):  # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    # def go_to(self, new_floor):
    #     floor = 0
    #     if new_floor < 1 or new_floor > self.number_of_floors:
    #         print(f'Извините, но такого этажа не существует')
    #     else:
    #         for floor in range(new_floor):
    #             print(floor + 1)


h1 = House("ЖК Медветково", 16)
h2 = House("Офис", 3)

# h1.go_to(4)
# h2.go_to(5)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
# __eq__
print(h1 == h2)
print(h1.__add__(4))
print(h2.__radd__(7))
print(h1.__iadd__(10))
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
