def linear_search(arr, target):
    """
    Perform linear search to find the index of the target element in the array.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target not found

# Example usage
arr = [5, 3, 8, 6, 2, 7, 1, 4]
target = 6
index = linear_search(arr, target)
if index != -1:
    print("Element", target, "found at index", index)
else:
    print("Element", target, "not found in the array")

"""
Theory Question:
Explain the concept of linear search and its role in computer science algorithms. 
Describe how linear search works, including its algorithmic complexity and best-case and worst-case scenarios. 
Discuss the advantages and disadvantages of linear search compared to other search algorithms, such as binary search.

Practical Question:
Design a Python program that demonstrates the use of linear search to find a specific element in a list. 
The program should have the following functionalities:

Allow the user to input a list of elements and a target element to search for.
Implement the linear search algorithm to find the index of the target element in the list.
Display the index of the target element if found or a message indicating that the element is not present in the list.
Include validation checks to ensure that the user inputs are in the correct format and that the linear search algorithm operates correctly for different scenarios.

"""