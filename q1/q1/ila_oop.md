# **ILA 3-1: Applying the Four Pillars of OOP**

**Section:** 9 - Platinum  
**Name:** Ace Philip Lee T. Mendoza  
**Date:** August 19, 2026

## **Sari-Sari Store Inventory System**

### **1. Encapsulation**

**Encapsulation means keeping related data and methods together inside an object. In the inventory system, a ****`Product`**** object can contain properties such as ****`nam`**`e`, `price`, and `quantity`, along with methods such as `addStock()` and `removeStock()`. This keeps the product's information organized and prevents other parts of the program from changing the data incorrectly. It also makes the program easier to maintain because the product's data and behaviors are grouped together.

### 2. Abstraction

Abstraction means showing only the important details of an object while hiding unnecessary implementation details. For example, the inventory system could have an `addProduct()` method that allows the user to add a product without needing to know how the program stores the product internally. This makes the system easier to use because the user only needs to interact with the necessary functions. It also makes the code less complicated and easier to understand.

### 3. Inheritance

Inheritance allows one class to receive properties and methods from another class. For example, a general `Product` class could contain the name, price, and quantity of a product, while classes such as `FoodProduct` and `HouseholdProduct` could inherit these properties. The child classes could then have additional properties or methods specific to their type. This reduces repeated code and makes the inventory system easier to expand.

### 4. Polymorphism

Polymorphism allows objects from different classes to use the same method in different ways. For example, different types of products could have a `displayInfo()` method, but each product type could display its information differently. A `FoodProduct` could display its expiration date, while a `HouseholdProduct` could display information about its category. This makes the program more flexible because the same method can work with different types of objects.

## Reflection

Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It would keep each product's name, price, and quantity organized inside a single object instead of using many separate variables. It would also allow methods such as `addStock()` and `removeStock()` to control how the inventory is changed. Overall, encapsulation would make the inventory system more organized, easier to manage, and easier to modify as the store adds more products.
