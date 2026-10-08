# Study Guide 8 - Encapsulation (Activity 1)
**Section:** 9 - Platinum  
**Name:** Ace Philip Lee T. Mendoza  
**Date:** October 8, 2026

## Activity 3: BankAccount.

### Overview and Requirements

This activity demonstrates the concept of **encapsulation,** a Object-Oriented Programming topic and mechanism using Python. Encapsulation is the process of keeping related data and methods together inside a class while controlling how the data/s can be accessed or modified. For this activity, a `BankAccount` class was created to protect sensitive account information and prevent invalid balance values within the class.

---

## Objectives of the Task

The program demonstrates the following concepts:

* Creating a class using Python
* Using private attributes
* Using setter methods to modify private data
* Using the `@property` decorator to create getter methods
* Validating data before changing an attribute
* Formatting a balance amount for display
* Creating and using an object from the class

---

## Needed Requirements

The `BankAccount` class contains:

1. A private `account_number` attribute
2. A private `balance` attributes
3. A setter for the account numbers
4. A setter for a balance
5. A getter for the account number using `@property`
6. A getter for the balance using `@property`
7. Validation that prevents the balance from becoming negative
8. A warning when a negative balance is attempted
9. An object that demonstrates the public methods
10. A formatted balance displayed in the output

---

## Encapsulation Used in the Program

The account information is stored using private attributes:

```python
self.__account_number
self.__balance
```

The double underscore makes these attributes private according to the access-modifier convention discussed in the study guide.
Instead of directly changing these attributes from outside the class, the program uses properties and setters.

For example:

```python
@property
def balance(self):
    return self.__balance
```

This allows the balance to be read through:

```python
account.balance
```

The balance can also be updated through its setter:

```python
@balance.setter
def balance(self, balance):
    if balance >= 0:
        self.__balance = balance
    else:
        print("Warning: Balance cannot be negative.")
```

This provides a layer of control over the data.

---

## Data Validation

The program does not allow a negative balance.

If the user attempts to assign a negative value:

```python
account.balance = -1000
```

The setter checks the value before changing the private balance. Since the value is negative, the program displays a warning and keeps the previous balance. This prevents invalid data from being stored in the objects.

---

## Why `@property` Is Used

The `@property` decorator allows getter methods to be accessed like normal attributes.

Instead of writing:

```python
account.get_balance()
```

the program will use:

```python
account.balances
```

This makes the code easier to read while still keeping the actual attribute private.

---

## Program Demonstrations

The program creates a `BankAccount` object:

```python
account = BankAccount("2026-001", 5000)
```

It then displays the account number and balance. 
The account number and balance are subsequently updated through their setters. 
Finally, the program attempts to assign a negative balance to demonstrate the validation system.

---

## Expected Output of the Program

A run of the program will produce output similar to:

```text
Bank Account Information
------------------------
Account Number: 2026-001
Balance: ₱5,000.00

After updating the account:
Account Number: 2026-002
Balance: ₱7,500.00

Testing negative balance:
Warning: Balance cannot be negative. The balance was not changed.
Current Balance: ₱7,500.00
```

The exact formatting

