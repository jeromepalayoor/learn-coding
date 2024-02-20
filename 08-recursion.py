# Factorial Calculation Using Recursion:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
print("Factorial of", number, "is", factorial(number))

# Fibonacci Sequence Using Recursion:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
terms = 10
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()

# Binary Search Using Recursion:
def binary_search(arr, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1

# Example usage
numbers = [2, 3, 5, 8, 11, 15, 17, 20]
target = 11
result = binary_search(numbers, 0, len(numbers) - 1, target)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

"""
Theory Question:
Explain the concept of recursion in computer science and its significance in problem-solving. Discuss how 
recursion works, including the base case and recursive case, and provide examples of problems that are 
commonly solved using recursion. Describe the advantages and disadvantages of recursion compared to iterative solutions.

Practical Question:
Design a Python program that demonstrates the use of recursion to solve a specific problem. The program should have the following functionalities:

Implement a recursive function to solve the chosen problem.
Provide options for the user to input parameters or data required for the recursive function.
Display the result obtained from the recursive function.
Include validation checks to ensure that the user inputs are in the correct format and that the recursive function operates correctly for different scenarios.

"""