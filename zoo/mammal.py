from zoo_manager import Animal

class Mammal(Animal):


    def __init__(self, name, species):
        super().__init__(name, species)

    
    def speak(self):
        pass

    def give_birth(self):
        print(f'{self.name} has given birth. Congrats.')



class Primate(Mammal):


    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print('*Angry monkey noises*')

    def climb_trees(self):
        print(f"{self.name} is climbing trees.")


class Marsupial(Mammal):


    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print('*Angry Aussie noises*')

    