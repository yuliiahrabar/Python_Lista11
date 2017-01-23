import animal

class Insect(animal.Animal):


    def __init__(self, age, height, weight, wings, stage):

        self.__wings = wings # czy ma skrzydła
        self.__stage = stage # typ rozwoju


    def set_wings(self, x):
        self.__wings = x

    def set_stage(self, x):
        self.__stage = x

    def get_wings(self):
        return self.__wings

    def get_stage(self):
        return self.__stage
