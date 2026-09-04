# OOPAct - Understanding Classes and Objects
**Section:** 9 - Platinum  
**Name:** Ace Philip Lee T. Mendoza  
**Date:** September 4, 2026
## Class Name

**Potion**

## Class Description

The `Potion` class represents a magical consumable item in a fantasy game (e.g Albion Online, Minecraft, etc). It stores information about the potion's name, effect, strength, and remaining uses, while allowing the player to use or modify the potion.

## Properties

| Property | Data Type | Description                                      |
| -------- | --------- | ------------------------------------------------ |
| name     | string    | The name of the potion                           |
| effect   | string    | Describes what the potion does                   |
| strength | int       | Indicates how powerful the potion's effect is    |
| uses     | int       | The number of times the potion can still be used |

## Methods

| Method                        | Description                                                      |
| ----------------------------- | ---------------------------------------------------------------- |
| usePotion()                   | Uses the potion and decreases its remaining uses by one          |
| increaseStrength(amount: int) | Increases the potion's strength by the specified amount          |
| displayInfo()                 | Displays the potion's name, effect, strength, and remaining uses |

## Class Diagram

<img width="1920" height="1080" alt="classDiagram" src="https://github.com/user-attachments/assets/db823448-c336-4166-8004-ade75f385fef" />

## Design Explanation

### Why did you choose this class?

I chose the `Potion` class because I wanted to design something from a fantasy game system. A potion is a useful example of a class because it has several properties and can perform different actions when used by a player.

### Which property is the most important? Why?

I think `uses` is the most important property because it determines how many times the potion can still be used. Without tracking its remaining uses, the game would not know when the potion has run out.

### Which method is the most useful? Why?

I think `usePotion()` is the most useful method because using the potion is its main purpose. The method also changes the `uses` property whenever the potion is consumed.
