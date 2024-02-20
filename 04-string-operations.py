# Example of common string operations

# String concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenated string:", concatenated_str)

# String slicing
original_str = "Python"
substring = original_str[1:4]
print("Substring:", substring)

# Length calculation
str_length = len(original_str)
print("Length of the string:", str_length)

# String methods
my_string = "    hello world    "
print("Original string:", my_string)
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Stripped string:", my_string.strip())

# String formatting
name = "Alice"
age = 25
formatted_str = "Hello, my name is {} and I am {} years old".format(name, age)

#####################################################

user_input = input("Enter a string: ")

# Print the length of the string
print("Length of the string:", len(user_input))

# Print the first character of the string
print("First character:", user_input[0])

# Print the last character of the string
print("Last character:", user_input[-1])

# Print the string in uppercase
print("Uppercase:", user_input.upper())

# Print the string in lowercase
print("Lowercase:", user_input.lower())

# Concatenate the string with itself and print the result
print("Concatenated with itself:", user_input + user_input)

# Print the substring from index 2 to index 5 (inclusive)
print("Substring from index 2 to index 5:", user_input[2:6])

# Check if the string contains a specific substring entered by the user
substring = input("Enter a substring to check: ")
if substring in user_input:
    print("The string contains the substring.")
else:
    print("The string does not contain the substring.")

"""
Theory Question:
Explain common string operations in Python. Discuss operations such as string concatenation, slicing, 
length calculation, and string methods. Provide examples for each operation.

Practical Question:
Write a Python program that prompts the user to enter their full name (first name and last name separated by a space). 
Then, perform the following operations:

Split the full name into first name and last name.
Print the first name and last name separately.
Count and print the number of characters in the first name and last name separately.
Print the initials of the first name and last name.
Check if the last name is "Smith" and print whether it is or not.

"""