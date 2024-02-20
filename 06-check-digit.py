# ISBN validation example

def validate_isbn(isbn):
    if len(isbn) != 13:
        return False
    if not isbn.isdigit():
        return False
    result = sum(int(isbn[i]) * (3 if i % 2 == 0 else 1) for i in range(12))
    check_digit = (10 - (result % 10)) % 10
    return check_digit == int(isbn[-1])

isbn = input("Enter the ISBN: ")
while not validate_isbn(isbn):
    print("Invalid ISBN. Please enter a valid 13-digit ISBN.")
    isbn = input("Enter the ISBN: ")

print("ISBN is valid!")

"""
Theory Question:
Explain the concept of check digit validation and its significance in data integrity. 
Describe how check digit validation works, providing an example algorithm such as the Luhn algorithm. 
Discuss common applications of check digit validation in real-world scenarios, 
highlighting its role in error detection and prevention.

Practical Question:
Design a Python program that implements check digit validation using the Luhn algorithm. 
The program should prompt the user to enter a numerical identifier (e.g., a credit card number or an identification number) 
with a check digit. Implement the necessary functions to calculate and validate the check digit based on the Luhn algorithm. 
After receiving input from the user, the program should determine whether the provided identifier with the 
check digit is valid or not and display an appropriate message.
"""