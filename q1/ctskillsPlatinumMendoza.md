Computational Thinking Exercise

Smart Vending Machine

Section: 9 - Platinum
Name:  Ace Philip Lee T. Mendoza
Date: August 11, 2026

Step 1: Identify the Big Problem

Main Problem
The vending machine has difficulty processing student purchases accurately and efficiently. It may give incorrect change, fail to notify users when items are out of stock, dispense the wrong item, and become slow when multiple students use it in succession.

Step 2: Identify the Sub-Problems

1. The machine sometimes gives students the wrong amount of change after a purchase.

2. The machine does not notify the user or staff when an item is out of stock.

3. Students may accidentally select the wrong item and receive a different product than intended.

4. The machine becomes slow when multiple students use it one after another.


Step 3: Define Computational Thinking Approaches

Sub-Problem 1: Incorrect Change
CT Skill: Algorithm Design
The machine can use a consistent sequence of steps to calculate the correct change by subtracting the item price from the amount of money inserted.

Sub-Problem 2: Items Run Out Without Notification
CT Skill: Abstraction
The machine can focus on the important information about each item's stock level. When the quantity reaches zero, it can display an "Out of Stock" message.

Sub-Problem 3: Students Select the Wrong Item
CT Skill: Pattern Recognition
The machine can identify common selection mistakes and reduce them by displaying clear item numbers, names, and confirmation messages before dispensing the product.

Sub-Problem 4: Machine Becomes Slow With Multiple Users
CT Skill: Decomposition
The purchasing process can be divided into smaller steps, such as item selection, payment, change calculation, and item dispensing. This makes each part easier to manage and improve.

Step 4: Algorithmic Solution
Selected Sub-Problem: Incorrect change is given after a purchase.

Pseudocode

START

Display available items and their prices.
Ask the student to select an item.
Get the price of the selected item.
Ask the student to enter the amount of money inserted.

IF amount inserted is greater than or equal to the item price THEN:
  Calculate change = amount inserted - item price.
  Dispense the selected item.
  Return the calculated change.

ELSE:
  Display "Insufficient payment."

END IF:
END

Reflection / Explanation:
Decomposition helps solve the vending machine problem by breaking one large problem into smaller and more manageable parts. Instead of trying to fix the entire machine at once, each issue can be addressed separately, such as calculating change, checking inventory, confirming selections, and improving the purchasing process. The CT skills used help make the solution more organized and reliable. Algorithm Design provides clear steps for calculating change, Abstraction focuses only on important stock information, Pattern Recognition helps identify common selection errors, and Decomposition separates the vending process into smaller tasks.

