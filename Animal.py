from add_animal import AddAnimal
import Bird

class Animal(AddAnimal):
    zoo_name = "San Diego Zoo"
    __count_animal = 0
    animals = []

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self._AddAnimal__add_animal()
        self.count_animal()

    @classmethod
    def count_animal(cls):
        cls.__count_animal += 1

    def make_sound(self):
        return self.sound

    def info(self):
        return (f"name:{self.name}\nspecies:{self.species}\n"
                f"age:{self.age}\nsound:{self.sound}")
    
    def _AddAnimal__add_animal(self):
        Animal.animals.append({"Zoo":Animal.zoo_name, "Name":self.name,
                               "Species":self.species, "Age":self.age,
                               "Sound":self.sound})

    def get_animals(self):
        return Animal.animals

    @classmethod
    def get_count(cls):
        return cls.__count_animal

    def __str__(self):
        return "Zoo Animal Information Management System"