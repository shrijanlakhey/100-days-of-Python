class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):# 'Animal' is a parent class that the 'Fish' class is inheriting from
    def __init__(self):
        super().__init__() # super = parent, the child class now inherits all the attributes and methods of the 'Fish' class
    
    def swim(self):
        print("Moving in water.")

    def breathe(self):
        super().breathe() # inheriting a method from the super class
        print("doing this underwater.")

nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)