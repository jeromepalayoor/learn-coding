# Example of a simple function definition and calling
def greet(name):
    print("Hello,", name)

greet("Alice")

"""
Structure of a function definition:

def <function_name>(<parameters>):
    <statements>
    return <value>

The return statement is optional and is used to return a value from the function.

The parameters are optional and are used to pass values to the function.

calling a function:
<function_name>(<arguments>)
"""

# Example of a function with a return statement
def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)

# Example of a function with default parameters
def greet(name="Alice"):
    print("Hello,", name)

greet()
greet("Bob")

# Example of a function with variable number of arguments
def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

result = add(1, 2, 3, 4, 5)
print("Result:", result)

# Example of a function with keyword arguments
def greet(name, message="Hello"):
    print(message, name)

greet("Alice")
greet("Bob", "Hi")

# Example of a function with variable number of keyword arguments
def greet(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

greet(name="Alice", message="Hello")
greet(name="Bob", message="Hi")

# Example of a recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
result = factorial(5)
print("Result:", result)

"""
Theory Question:
Explain the concept of functions in Python. Discuss the benefits of using functions in programming, 
and describe how they can help in organizing and reusing code. 
Provide an example of a simple function definition and invocation.

Practical Question:
Write a Python program that defines a function called calculate_area to calculate the area of a circle. 
The function should take the radius of the circle as input and return the area. Then, prompt the user to 
enter the radius of a circle and use the calculate_area function to compute and print the area of the circle.
"""