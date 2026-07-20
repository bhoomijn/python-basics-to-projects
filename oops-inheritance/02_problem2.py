# animal_pet_dog_inheritance.py
# Demonstrates multilevel inheritance in Python (Animal → Pet → Dog)

class Animal:
    def __init__(self, name):
        self.name = name


class Pet(Animal):
    def __init__(self, name, owner):
        super().__init__(name)   # call parent constructor
        self.owner = owner


class Dog(Pet):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed

    @staticmethod
    def bark():
        print("Woof! Woof!")


# Object creation
dog1 = Dog("Tommy", "Devendra", "German Shepherd")

# Accessing attributes
print(f"Dog's Name: {dog1.name}")
print(f"Owner: {dog1.owner}")
print(f"Breed: {dog1.breed}")

# Calling method
dog1.bark()   # Output: Woof! Woof!


# animal_pet_dog_inheritance.py
# Demonstrates multilevel inheritance with multiple methods

class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    @staticmethod
    def bark():
        print("The dog is making noise like bhow bhoww")

    # Instance method
    def play(self):
        print("The dog is playing happily!")


# Object creation
d = Dog()

# Calling static method
d.bark()   # Output: The dog is making noise like bhow bhoww

# Calling instance method
d.play()   # Output: The dog is playing happily!

