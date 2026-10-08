"""
Study Guide 8 - Encapsulation
Activity 3: BankAccount
Section: 9 - Platinum
Name: Ace Philip Lee T. Mendoza
Date: October 8, 2026

"""


class BankAccount:
    #Represents bank account with protected account information using the necesarry functions.

    def __init__(self, account_number, balance):
        #Create a bank account with an account number and starting balance.
        self.__account_number = account_number
        self.__balance = 0
        # Usea the setter so the starting balance is also validated.
        self.balance = balance

    @property
    def account_number(self):
        #Return the account number back.
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        #Update the account number
        self.__account_number = account_number

    @property
    def balance(self):
        #Return the current account balance.
        return self.__balance

    @balance.setter
    def balance(self, balance):
        
        #Update the account balance. 
      #Negative balances are not allowed. If a negative value is given, the old balance is kept and a warning is displayed for the user.
        
        if balance >= 0:
            self.__balance = balance
        else:
            print("Warning: Balance cannot be negative. "
                  "The balance was not changed.")


# Create an object of the BankAccount class.
account = BankAccount("2026-001", 5000)

# Display the account information using the public properties.
print("Bank Account Information")
print("------------------------")
print("Account Number:", account.account_number)
print(f"Balance: ₱{account.balance:,.2f}")

# Update ccount number using its setter.
account.account_number = "2026-002"

# Update the balance using its setter thingy.
account.balance = 7500

print("\nAfter updating the account:")
print("Account Number:", account.account_number)
print(f"Balance: ₱{account.balance:,.2f}")

# Try to set a negative balance.
print("\nTesting negative balance:")
account.balance = -1000# The balance remains unchanged because the setter rejected it.
print(f"Current Balance: ₱{account.balance:,.2f}")
