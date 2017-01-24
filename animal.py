class Animal:

    def __init__(self, name, age, height, weight):
        """Inicjuje zwierzę"""

        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def set_age(self, x):
        self.__age = x

    def set_height(self, x):
        self.__height = x

    def set_weight(self, x):
        self.__weight = x

    def __str__(self):
        return "{}: age = {}, height = {}, weight = {}".format(self.__name, self.__age, self.__height, self.__weight)

