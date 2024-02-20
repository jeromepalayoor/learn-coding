# Validation in registration system example

def validate_name(name):
    if not name:
        return False
    return all(char.isalpha() or char.isspace() for char in name)

def validate_password(password):
    if not password:
        return False
    return len(password) >= 6 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)

name = input("Enter your name: ")
while not validate_name(name):
    print("Invalid name. Please enter a valid name.")
    name = input("Enter your name: ")

password = input("Enter your password: ")
while not validate_password(password):
    print("Invalid password. Please enter a password with at least 6 characters and containing both letters and numbers.")
    password = input("Enter your password: ")

print("Registration successful!")


"""
Theory Question:
Describe the concept of validation workflow in software development. 
Explain the importance of validation in ensuring data integrity and user input correctness. 
Discuss common techniques and best practices for implementing validation workflows in Python applications.

Practical Question:
Create a Python program for a simple quiz game that validates user input for answers.

The program should have the following functionalities:

Define a list of quiz questions along with their correct answers.
Display each quiz question to the user and prompt them to enter their answer.
Implement validation checks for user input to ensure that it is in the correct format and matches the available options or answers.
If the user's input is valid and matches the correct answer, display a success message and move to the next question.
If the user's input is invalid or incorrect, display an appropriate error message and prompt the user to try again.
After the user completes all the quiz questions, display their total score.

"""