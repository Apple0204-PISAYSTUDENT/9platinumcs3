# My OOP Seed System - Part III: Connecting Your Objects

**Section:** 9 - Platinum

**Name:** Ace Philip Lee T. Mendoza

**Date:** September 18, 2026

---

## Step 1 - Review Your Existing System

### 1. What Classes Currently Exist?

The current system contains two classes:

* `Potion`
* `Tome`

The `Potion` class represents individual potions and contains attributes such as name, effect, strength, and number of uses. The `Tome` class represents a book that stores and manages multiple `Potion` objects.

### 2. What Problem or Limitation Exists in the Current Design?

One limitation is that the current system only has a basic association between `Tome` and `Potion`. The system does not yet use inheritance to represent different types of potions, so adding specialized potion types could lead to repeated code if each type were created as a completely separate class. The system can also be improved by explicitly modeling the ownership relationship between the Tome and the Potion objects.
              
              Potion
                 △
                 |
          HealingPotion
## Step 3 - Create a Child Class

**Parent Class is:**
`Potion`

**Child Class is:**
`HealingPotion`

**Why is the child a type of the parent?**

A `HealingPotion` is a Type of `Potion` because it has the same basic characteristics and behaviors as a regular Potion. It has a name, effect, strength, and number of uses, and it can use the methods inherited from the `Potion` class. The `HealingPotion` class is more specific because it can also have an additional attribute, such as `healing_amount`, that describes how much health it can restore.
