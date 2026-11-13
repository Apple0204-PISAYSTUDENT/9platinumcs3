# Activity 2: Duck Typing
**Section:** 9 - Platinum  
**Name:** Ace Philip Lee T. Mendoza  
**Date:** November 13, 2026

**Python File:** `Polymorphism_Activity 2.py`

## 1. Answer the following questions

**a. What is duck typing, as explained in the video?**

Duck typing is a concept in Python where an object can be used based on the methods it has rather than the class it belongs to. As long as an object has the required method, Python can use it. In simply words, we need to look at what an object can do, before undergoing the process of classification. For example, if a zoo keeper of an animal checkpoint looks for animals who can fly, eagles, bats, and bees, despite being different animals, pass through the checkpoint, while any other animals who can't fly cannot pass. 

**b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?**

The Car class basically needed to have the same method that the loop calls in the Dog and Cat classes. This allows it to work in the same loop without inheriting from the Animal class. 

## 2. Python Code

The program creates three classes: Car, Boat, and Drone. Each class has its own implementation of the `move()` method, different outputs, same method

A function named `start_trip(vehicle)` calls the `move()` method of the given object. Since every object has the method, they all pass this 'checkpoint'.

See the accompanying Python code.

## 3. How does the code in 2.2 demonstrate polymorphism?

The code demonstrates polymorphism because different objects use the same method name, `move()`, but produce different outputs. Each object performs its own action depending on its class, even without using inheritance.

## Conclusion

Duck typing allows different objects to share the same functionality through common method names without requiring them to inherit from the same parent class. Basically, we don't look at something based on what they look like, smell, taste, feel, and more, but on what they can do. If An animal can quack, lay eggs, fly, and has a bill, then it is a duck.
