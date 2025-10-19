from src import Animal, Bird

if __name__ == "__main__":
    parrot = Bird.Bird("parrot", "Rose-ringed", 2, "sound.mp3", 12)
    lion = Animal.Animal("lion", "large cat", 23, "ROAR!")
    print(lion.get_count())
    print(parrot.get_count())
    print(parrot.info())
    print(lion.info())
    print(parrot.get_animals())
    parrot.make_sound()