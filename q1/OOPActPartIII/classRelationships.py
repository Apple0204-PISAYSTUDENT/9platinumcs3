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


class Tome:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []
        self.is_open = False

    def open(self):
        self.is_open = True
        print(self.title, "has been opened.")

    def close(self):
        self.is_open = False
        print(self.title, "has been closed.")

    def addPotion(self, potion):
        self.contents.append(potion)
        print(potion.name, "was added to", self.title + ".")

    def displayContents(self):
        print("\nContents of", self.title + ":")

        if len(self.contents) == 0:
            print("The Tome contains no potions.")
        else:
            for potion in self.contents:
                print("-", potion.name)
                print("  Effect:", potion.effect)
                print("  Strength:", potion.strength)


# CREATE OBJECTS

potion1 = Potion(
    "Phoenix Elixir",
    "Restores health",
    50,
    3
)

potion2 = Potion(
    "Frost Draught",
    "Slows enemies",
    30,
    5
)

potion3 = Potion(
    "Shadow Tonic",
    "Improves stealth",
    40,
    4
)

tome = Tome(
    "The Alchemist's Tome",
    "Eldrin"
)


# BEFORE RELATIONSHIP

print("--- BEFORE RELATIONSHIP ---")

print("Tome:", tome.title)
print("Author:", tome.author)
print("Number of potions:", len(tome.contents))

print("\nPotion Objects:")

potion1.displayInfo()

print()

potion2.displayInfo()

print()

potion3.displayInfo()


# BUILDING RELATIONSHIP

print("\n--- BUILDING RELATIONSHIP ---")

tome.addPotion(potion1)
tome.addPotion(potion2)
tome.addPotion(potion3)


# AFTER RELATIONSHIP

print("\n--- AFTER RELATIONSHIP ---")

print("Tome:", tome.title)
print("Author:", tome.author)
print("Number of potions:", len(tome.contents))

tome.displayContents()


# ACCESSING DATA THROUGH THE RELATIONSHIP

print("\n--- ACCESSING DATA THROUGH RELATIONSHIP ---")

for potion in tome.contents:
    print(potion.name, "has", potion.strength, "strength.")


# USING A RELATED OBJECT THROUGH THE TOME

print("\n--- USING A POTION THROUGH THE TOME ---")

tome.contents[0].usePotion()

print("\nUpdated Phoenix Elixir:")

tome.contents[0].displayInfo()


# TOME OPEN/CLOSE

print("\n--- TOME STATUS ---")

tome.open()
tome.close()
