class Animal: #Animal Class thingy with functions tat will be used and inherited by subclasses, which are the named aniimals
    def __init__(self, name):
        self.name = name #Now has name as its variable

    def eat(self):
        print(self.name, "eats.") #the eating mechanisms

    def make_sound(self): #the sounds
        print(self.name, "makes a sound.")


class Lion(Animal): #The Lion with eating fresh meat and roar as its unique functions
    def eat(self):
        print(self.name, "eats fresh meat.") #Self.name gets the name of the animal, and the prints "eats fresh meat."

    def make_sound(self):
        print(self.name, "roars loudly!") #Again gets name, and prints the text, same goes for the elephant and monkey


class Elephant(Animal):
    def eat(self):
        print(self.name, "eats grass and fruits.")

    def make_sound(self):
        print(self.name, "trumpets!")


class Monkey(Animal):
    def eat(self):
        print(self.name, "eats bananas.")

    def make_sound(self):
        print(self.name, "chatters!")

#Names of the animals
lion = Lion("Simba")
elephant = Elephant("Dumbo") #The guy below is talking about us
monkey = Monkey("George")

animals = [lion, elephant, monkey]

for animal in animals: #Makes the compilation and entire output of all animals by calling upon the set of named animals provided here
    animal.make_sound()
    animal.eat()
    print("-----")
