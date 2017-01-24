import animal
import bird
import fish
import insect
import gc

def create_Animal(name, age, height, weight):
    """Tworzy obiekt klasy Animal"""
    return animal.Animal(name, age, height, weight)

def create_Fish(name, age, height, weight, type_of_fins, type_of_water):
    """Tworzy obiekt klasy Fish"""
    return fish.Fish(name, age, height, weight, type_of_fins, type_of_water)

def create_Insect(name, age, height, weight, wings, stage):
    """Tworzy obiekt klasy Insect"""
    return insect.Insect( name, age, height, weight, wings, stage)

def create_Bird(name, age, height, weight, type_of_wings, type_of_beak):
    """Tworzy obiekt klasy Bird"""
    return bird.Bird(name, age, height, weight, type_of_wings, type_of_beak)

def delete_object(obj):
    """Usuwa  obiekt"""
    del obj


kotek = create_Animal("Kotek", 5,10,15)
pies = create_Animal("Pies", 2,10,15)
ryba = create_Fish("Ryba", 1,10,10,2,"sea water")
biedronka = create_Insect("Biedronka", 0.3, 0.1, 0.1, "tak", 2)
parus = create_Bird("Parus", 1, 1, 1, 1, 1)

for obj in gc.get_objects():
    if isinstance(obj, animal.Animal):
        print(obj)

