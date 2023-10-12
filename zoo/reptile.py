from zoo_manager import Animal

class Reptile(Animal):


    def __init__(self, name, species):
        super().__init__(name, species)

    def speak(self):
        print('*Angry reptile noises*')

    def bask_in_sun(self):
        print(f"{self.name} is basking in the sun.")