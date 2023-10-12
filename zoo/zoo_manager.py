from abc import ABC, abstractmethod

class Animal(ABC):


    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    # @abstractmethod
    def speak(self):
        return 'Animal sound'


class Mammal(Animal):


    def __init__(self, name, species):
        super().__init__(name, species)

    
    def speak(self):
        pass

    def give_birth(self):
        return f'{self.name} the {self.species} has given birth'



class Primate(Mammal):


    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print('*Angry monkey noises*')

    def climb_trees(self):
        return f"{self.name} the {self.species} is climbing trees"


class Marsupial(Mammal):


    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print('*Angry Aussie noises*')

    def carry_baby(self):
        return f'{self.name} the {self.species} is carrying its baby'


class Bird(Animal):


    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def speak(self):
        print('CAW CAW!!!!!')


class Aviary(Bird):

    def __init__(self):
        self.birds = []
        # self.birds.append(bird)


class Reptile(Animal):


    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print('*Angry reptile noises*')

    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"

class ReptileEnclosure(Reptile):

    def __init__(self):
        self.reptiles = []
        # self.enclosure.append(reptile)