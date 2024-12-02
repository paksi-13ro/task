class Vehicle:
    __COLOR_VARIANTS = ['Синмй', 'Красный', 'Черный', 'Белый', 'Серый', 'Голубой']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color.upper()}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}\n')

    def set_color(self, new_color):

        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS]
        if new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


a1 = Sedan('Олег', 'Reno Logan', 109, 'Белый')

a1.print_info()

a1.set_color('Оранжевый')
a1.set_color('Черный')
a1.owner = 'Антон'

a1.print_info()
