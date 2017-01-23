import animal

class Bird(animal.Animal):


    def __init__(self, age, height, weight, type_of_wings, type_of_beak):

        self.__type_of_wings = type_of_wings # rodzaj skrzydeł
        self.__type_of_beak = type_of_beak # rodzaj dzióbu


    def set_type_of_wings(self, x):
        self.__type_of_wings = x

    def set_type_of_beak(self, x):
        self.__type_of_beak = x

    def get_type_of_wings(self):
        return self.__type_of_wings

    def get_type_of_beak(self):
        return self.__type_of_beak
