class Potion:
    def __init__(self, name, effect, strength, uses):
        self.name = name
        self.effect = effect
        self.strength = strength
        self.__uses = uses

    def usePotion(self):
        if self.__uses > 0:
            self.__uses -= 1
            print(self.name, "was used.")
        else:
            print("No uses left.")

    def increaseStrength(self, amount):
        self.strength += amount

    def displayInfo(self):
        print("Name:", self.name)
        print("Effect:", self.effect)
        print("Strength:", self.strength)
        print("Uses:", self.__uses)


# Two Potion objects
potion1 = Potion("Phoenix Elixir", "Restores health", 50, 3)
potion2 = Potion("Frost Draught", "Slows enemies", 30, 5)

print("Potion 1:")
potion1.displayInfo()

print("\nPotion 2:")
potion2.displayInfo()

# Change Potion 1
potion1.usePotion()

print("\nAfter using Potion 1:")
potion1.displayInfo()

print("\nPotion 2 stays the same:")
potion2.displayInfo()
