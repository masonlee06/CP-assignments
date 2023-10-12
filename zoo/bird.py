from zoo_manager import Animal

class Bird(Animal):


    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def speak(self):
        print('CAW CAW!!!!!')