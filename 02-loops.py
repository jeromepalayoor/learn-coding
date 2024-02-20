# Example of for loop
for i in range(1, 5):
    print("Iteration", i)

"""
Structure of for loop:

for <variable> in <sequence>:
    <statements>
else:
    <statements>

The else block is optional and is executed when the loop terminates normally (i.e., not by a break statement).

The sequence can be a list, a tuple, a string, a set, or a dictionary.

The range() function returns a sequence of numbers, starting from 0 by default, 
and increments by 1 (by default), and stops before a specified number.

The range() function can take up to three arguments: range(start, stop, step).
"""

# Example of while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

"""
Structure of while loop:

while <condition>:
    <statements>
else:
    <statements>

The else block is optional and is executed when the loop terminates normally (i.e., not by a break statement).
"""

"""
Theory Question:
Differentiate between for and while loops in Python. Explain when each type of loop would be more
appropriate to use, and provide an example for both types.


Practical Question:
Write a Python program that asks the user to enter a positive integer and then uses a for loop
to calculate and print the factorial of that number. Ensure that your program handles cases
where the input is not a positive integer.

Additionally, write another Python program that accomplishes the same task using a while loop instead of a for loop.
"""