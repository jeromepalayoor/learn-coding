# learn conditional statements (if, else, elif)

# simple program to check if a number is odd or even
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

"""
structure of a if else statement:

if <condition>:
    <code that runs if condition is true>
else:
    <code that runs if condition is false>
"""

# simple program to check if a person is eligible to vote
age = int(input("Enter your age: "))

if age >= 21:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# check if a year is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # can chain multiple conditions into it
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

"""
structure of a if, elif, else statement

if <condition-1>:
    <code that runs if condition-1 is true>
elif <condition-2>:
    <code that runs if condition-1 is false but condition-2 true>
else:
    <code that runs if both condition-1 and condition-2 is true>
"""

# simple program to determine largest number between 3 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is ", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is", num2)
else:
    print("The largest number is", num3)

"""
Theory question:
Explain the difference between 'if', 'elif', and 'else' statements in Python. Provide an example for each.

Practical question:
Write a Python program that asks the user to input their score for a test (out of 100) and then prints out their 
grade based on the following criteria:

A: 70 - 100
B: 60 - 69
C: 55 - 59
D: 50 - 54
E: 45 - 49
S: 40 - 44
U: 0 - 39

Make sure to handle cases where the input score is not within the valid range.
"""

# GOOD LUCK!