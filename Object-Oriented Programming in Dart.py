# Define an interface
class Animal:
    def make_sound(self):
        pass

# Define a class that implements the Animal interface
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Define a class that inherits from Dog and overrides the make_sound method
class LoudDog(Dog):
    def make_sound(self):
        return super().make_sound().upper()

# Define a class that represents an instance initialized with data from a file
class AnimalFromFile(Animal):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.sound = file.readline().strip()

    def make_sound(self):
        return self.sound

# Method demonstrating the use of a loop
def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

# Example usage
if __name__ == "__main__":
    animals = [Dog(), LoudDog(), AnimalFromFile('animal_data.txt')]
    animal_sounds(animals)
