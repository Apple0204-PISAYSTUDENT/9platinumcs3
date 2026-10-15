
# SG 9 – Inheritance: Library Management System

**Subject:** Computer Science 3  
**Quarter:** Quarter 2  
**Assessment:** Formative Assessment No. 1  
**Python File:** `q2_FA1_Code.py`

## I. Introduction

The Library Management System is a Python program that demonstrates the concept of inheritance in Object-Oriented Programming (OOP). It uses a parent class named `Publication` and two child classes named `Book` and `Magazine`.

The program stores information about publications, displays their details, and validates page counts and issue numbers to ensure that they contain positive integer values.

## II. Objectives

- Implement inheritance using parent and child classes.
- Use constructors to initialize object attributes.
- Apply encapsulation using private attributes.
- Implement getter and setter methods.
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
                  |
          -----------------
          |               |
         Book          Magazine
         ----          --------
         number_of_     issue_number
         pages          --------
         --------       get_issue_number()
         get_number_    set_issue_number()
         of_pages()
         set_number_
         of_pages()
         display_info()
```

## V. Program Features

The program implements the following features:

1. Creates two objects of the `Publication` class.
2. Creates two objects of the `Book` class.
3. Creates two objects of the `Magazine` class.
4. Displays the information of all six objects.
5. Uses inheritance to reuse common attributes and methods.
6. Uses `super()` to call methods from the parent class.
7. Uses private attributes to demonstrate encapsulation.
8. Validates page counts and issue numbers.
9. Tests invalid values to demonstrate error handling.

## VI. Data Validation

The program checks whether the number of pages and issue number are positive integers.

Examples of invalid values include:
- `0`
- Negative integers, such as `-5`
- Non-integer values

When an invalid value is provided, the program displays an appropriate message.

Example output:

```text
The number of pages must be positive.
The issue number must be positive.
```

The setter methods preserve the existing valid values when an invalid update is attempted.

## VII. How to Run the Program

1. Save the Python code as `sg9_inheritance.py`.
2. Open a terminal or command prompt in the folder containing the file.
3. Execute the following command:

```bash
python sg9_inheritance.py
```

If necessary, use:

```bash
python3 sg9_inheritance.py
```

The program does not require external libraries.

## VIII. Object-Oriented Programming Concepts

### Inheritance

Inheritance allows the `Book` and `Magazine` classes to reuse the attributes and methods defined in the `Publication` class.

### Encapsulation

Encapsulation is demonstrated through private attributes, such as `__title`, `__author`, `__number_of_pages`, and `__issue_number`.

### Constructors

Constructors initialize an object's attributes when it is created.

### The `super()` Function

The `super()` function allows child classes to call the constructor and methods of their parent class.

### Getters and Setters

Getters retrieve attribute values, while setters validate and update attribute values.

## IX. Conclusion

The Library Management System demonstrates how inheritance can make Python programs more organized, reusable, and easier to maintain. By using `Publication` as the parent class, `Book` and `Magazine` inherit common functionality while maintaining their own specialized attributes.

The project also demonstrates encapsulation, constructors, getters, setters, and data validation. These concepts help create a structured program that manages publication information and handles invalid input appropriately.

## X. Portfolio Update

The following files should be included in the CS3 portfolio repository:

- `sg9_inheritance.py` – Python source code for the Library Management System.
- `sg9_inheritance.md` – Documentation describing the program, its class structure, and its features.

The main `README.md` should also be updated to include the activity title, a short description, and links to both files.

