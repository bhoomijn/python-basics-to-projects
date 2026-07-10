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
