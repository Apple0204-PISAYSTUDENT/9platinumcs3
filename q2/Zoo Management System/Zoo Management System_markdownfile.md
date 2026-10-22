# Method Overriding in a Zoo Management System

**Section:** 9 - Platinum  
**Name:** Ace Philip Lee T. Mendoza  
**Date:** October 22, 2026

**Python File:** `Zoo Management System_markdownfile.py`


## The Python Code

```python
# Parent class of the other classes
class Animal:
    def __init__(self, name): #the name, which is an attribute of animals
        self.name = name

    def eat(self): 
        print(self.name, "eats.") #Some methods and functions it has, like eating and making noise

    def make_sound(self):
        print(self.name, "makes a sound.")


# Child class: Lion, 
class Lion(Animal):
    def eat(self):
        print(self.name, "eats fresh meat.") #takes the attribute of name and uses the animal parent class original  
                                             #function, and places it in this text that will pop up, same applies to
                                             #everything else.

    def make_sound(self):
        print(self.name, "roars loudly!") #the sound, takes the name, text, print, so on, like the eat function


# Child class: Elephant
class Elephant(Animal):
    def eat(self):
        print(self.name, "eats grass and fruits.")

    def make_sound(self):
        print(self.name, "trumpets!")


# Child class: Monkey
class Monkey(Animal):
    def eat(self):
        print(self.name, "eats bananas.")

    def make_sound(self):
        print(self.name, "chatters!")


# Create objects/animals with their assigned attributes or name
lion = Lion("Simba")
elephant = Elephant("Dumbo") #the animals
monkey = Monkey("George")

# Call the methods using a for loop so that all animals use the animal classes methods
animals = [lion, elephant, monkey]

for animal in animals: #Cycles through the list of animals
    animal.make_sound()
    animal.eat()
    print("-----")
```

## Expected Output

```text
Simba roars loudly!
Simba eats fresh meat.
-----
Dumbo trumpets!
Dumbo eats grass and fruits.
-----
George chatters!
George eats bananas.
-----
#Yay
```

## Explanation

The `Animal` class is the parent class that contains the general `eat()` and `make_sound()` methods. The `Lion`, `Elephant`, and `Monkey` classes inherit from `Animal` and override these methods to display their specific eating habits and sounds, which are essentially innate abilities they possess that makes them different from one another but still follow the core functions of an animal.

The program creates one object for each child class and stores them in a list. A `for` loop calls both methods for every object.

**Method overriding** allows a child class to provide its own implementation of a method inherited from its parent class. This allows different animals to use the same method names while producing different outputs, which again, gives them the uniqueness that sets them apart from other sub classes, yet still adhere to the basic functions of their parent class.
