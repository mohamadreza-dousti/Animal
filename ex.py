from src import Animal, Bird

if __name__ == "__main__":
    parrot = Bird.Bird("kdjl", "kdjl", 2, "sound.mp3", 12)
    lion = Animal.Animal("lion", "kaka", 2, "hahaha")
    bird = Bird.Bird("kl", "kl", 2, "sound.mp3", 12)
    print(lion.get_count())
    print(parrot.get_count())
    print(parrot.info())
    print(lion.info())
    print(parrot.get_animals())
    parrot.make_sound()