import animal

class Fish(animal.Animal):


    def __init__(self, age, height, weight, type_of_fins, type_of_water):

        self.__type_of_fins = type_of_fins # rodzaj płetw
        self.__type_of_water = type_of_water # rodzaj wody


    def set_type_of_fins(self, x):
        self.__type_of_fins = x

    def set_type_of_water(self, x):
        self.__type_of_water = x

    def get_type_of_fins(self):
        return self.__type_of_fins

    def get_type_of_water(self):
        return self.__type_of_water
