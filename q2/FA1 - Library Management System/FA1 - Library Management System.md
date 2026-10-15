
# SG 9 – Inheritance: Library Management Systems 

**Section:** 9 - Platinum  
**Name:** Ace Philip Lee T. Mendoza  
**Date:** October 15, 2026
**Assessment:** Formative Assessment No. 1  
**Python File:** `q2_FA1_Code.py`

## I. Introduction

The Library Management System is a Python program that demonstrates the concept of inheritance in Object-Oriented Programming (OOP). It uses a parent class named `Publication` and two child classes named `Book` and `Magazine`. Essentially a form of Class Mitosis that creates to new classes that connect with the main file's attributes. The program stores information about publications, displays their details, and validates page counts and issue numbers to ensure that they contain positive integer values and reject negative integer values.

## II. Objectives

- Implement inheritance using parent and child classes.
- Use constructors to initialize and assign object attributes.
- Apply encapsulation using private attributes to ensure information is received correctly.
- Implement getter and setter methods for.
- Validate page counts and magazine issue numbers.
- Create and display two objects for each class.

## III. Class Descriptions

### 1. Publication Class

The `Publication` class serves as the parent class. It contains the common attributes shared by books and magazines.

**Attributes:**
- `title`
- `author`

**Methods:**
- `__init__()` initializes the publication's attributes.
- `get_title()` returns the title.
- `get_author()` returns the author.
- `set_title()` updates the title if it is valid.
- `set_author()` updates the author if it is valid.
- `display_info()` displays the publication's information.

### 2. Book Class

The `Book` class inherits from `Publication`. It adds a specialized attribute for storing the number of pages.

**Additional Attribute:**
- `number_of_pages`

The setter method checks whether the page count is a positive integer. If the value is invalid, the program displays an error message.

### 3. Magazine Class

The `Magazine` class also inherits from `Publication`. It adds an attribute for identifying a magazine's issue number.

**Additional Attribute:**
- `issue_number`

The setter method ensures that the issue number is a positive integer.

## IV. Class Diagram

```text
             Publication
             -----------
             title
             author
             -----------
                get_title()
             get_author()
             set_title()
             set_author()
             display_info()
          -----------------
          |            |
         Book          Magazine
         ----          --------
         number_of_     issue_number
         pages       --------
         ------       get_issue_number()
         get_number_    set_issue_number()
         of_pages()
         set_number_
         of_pages()
         display_info()
```

## V. Program Features

The program implements the following features:

1. Creates two objects of the `Publication` class.
2. Creates two object of the `Book` class.
3. Creates two objects of the `Magazine` class.
4. Displays the information of all six objects.
5. Uses inheritance to reuse common attributes and methods.
6. Uses `super()` to call methods from the parent class.
7. Uses private attributes to demonstrate encapsulation.
8. Validates page counts and issue numbers.
9. Tests invalid values to demonstrate error handling.

## VI. Data Validations

The program checks whether the number of pages and issue number are positive integers.

Examples of invalid values include:
- `0`
- Negative integers, such as `-5` and so on.
- Non-integer values (e.g 3.14, 9.8, 66.67,...)

When an invalid value is provided, the program displays an appropriate message.

Example output:

```text
The number of pages must be positive.
The issue number must be positive.
```

The setter methods preserve the existing valid values when an invalid update is attempted.

## VII. How to Run the Program

1. Save the Python code as `q2_FA1_Code.py`.
2. Open a terminal or command prompt in the folder containing the file.
3. Execute.

The program does not require external libraries.

## VIII. Object-Oriented Programming Concepts

### Inheritance

Inheritance allows the `Book` and `Magazine` classes to reuse the attributes and methods defined in the `Publication` father class.

### Encapsulation

Encapsulation is demonstrated through a collection of private attributes, such as `__title`, `__author`, `__number_of_pages`, and `__issue_number`. Which restricts them as private variables to edited within certain condition parameters.

### Constructors

Constructors initialize an object's attributes when it is created.

### The `super()` Function

The `super()` function allows child classes to call the constructor and methods of their parent class. 

### Getters and Setters

Getters retrieve attribute values, while setters validate and update attribute values with some setters needing specific conditions to fulfill before it can be updated or manipulating inputted data into a different data through conversion.

## IX. Conclusion

The Library Management System demonstrates how inheritance can make Python programs more organized, reusable, and easier to maintain. By using `Publication` as the parent class, `Book` and `Magazine` inherit common functionality while maintaining their own specialized attributes. Which can be associated closely to a form of "Class Mitosis."

The project also demonstrates encapsulation, constructors, getters, setters, and data validation. These concepts help create a structured program that manages publication information and handles invalid input appropriately.


