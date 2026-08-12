**Chinese Zodiac Code Exercise**

Section: 9 - Platinum  
Name: Ace Philip Lee T. Mendoza  
Date: August 12, 2026
Requirements:
A. Input
Ask the user to enter a year of birth, using 1900 as the baseline year.

B. Input Validation
The year entered by the user must not be earlier than 1900.

C. Invalid Input
If the user enters a year earlier than 1900, it will display an appropriate error message and stop the program.

D. Chinese Zodiac
Determine the Chinese Zodiac sign based on the year of birth. The zodiac signs repeat every 12 years, starting with Rat in 1900.

The order is:
1. Rat (鼠 / Shǔ)
2. Ox (牛 / Niú)
3. Tiger (虎 / Hǔ)
4. Rabbit (兔 / Tù)
5. Dragon (龙 / Lóng)
6. Snake (蛇 / Shé)
7. Horse (马 / Yáng)
8. Goat (羊 / Yáng)
9. Monkey (猴 / Hóu)
10. Rooster (鸡 / Jī)
11. Dog (狗 / Gǒu)
12. Pig (猪 / Zhū)

E. Year Consideration
Only the year of birth should be considered.
Python Code

```python
birth_year = int(input("Enter your birth year: "))

if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    zodiac = zodiac_signs[(birth_year - 1900) % 12]

    print("Your Chinese Zodiac Sign is:", zodiac)
