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


class HealingPotion(Potion):
    def __init__(self, name, effect, strength, uses, healing_amount):
        super().__init__(name, effect, strength, uses)
        self.healing_amount = healing_amount

    def heal(self):
        print(self.name, "restores", self.healing_amount, "health.")

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

# ==============================
# STEP 10 - TEST YOUR SYSTEM
# ==============================

print("===== TEST 1: INHERITANCE =====")

healingPotion1 = HealingPotion(
    "Healing Elixir",
    "Restores health",
    8,
    3,
    50
)

print("\nHealing Potion Information:")
healingPotion1.displayInfo()

print("\nChild-specific method:")
healingPotion1.heal()


print("\n===== TEST 2: AGGREGATION =====")

phoenixElixir = Potion(
    "Phoenix Elixir",
    "Revives the user",
    10,
    2
)

frostDraught = Potion(
    "Frost Draught",
    "Freezes the target",
    7,
    4
)

alchemistTome = Tome(
    "The Alchemist's Tome",
    "Eldrin"
)

alchemistTome.addPotion(phoenixElixir)
alchemistTome.addPotion(frostDraught)
alchemistTome.addPotion(healingPotion1)

print("\nTome Information:")
print("Title:", alchemistTome.title)
print("Author:", alchemistTome.author)

alchemistTome.displayContents()
