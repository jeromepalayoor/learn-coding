def binary_search(arr, target):
    """
    Perform binary search to find the index of the target element in the sorted array.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 6
index = binary_search(arr, target)
if index != -1:
    print("Element", target, "found at index", index)
else:
    print("Element", target, "not found in the array")

"""
Theory Question:
Explain the concept of binary search and its significance in computer science algorithms. 
Describe how binary search works, including its algorithmic complexity and the requirement of a sorted array. 
Discuss the advantages and disadvantages of binary search compared to other search algorithms, such as linear search.

Practical Question:
Design a Python program that demonstrates the use of binary search to find a specific element in a sorted list. The program should have the following functionalities:

Allow the user to input a sorted list of elements and a target element to search for.
Implement the binary search algorithm to find the index of the target element in the sorted list.
Display the index of the target element if found or a message indicating that the element is not present in the list.
Include validation checks to ensure that the user inputs are in the correct format and that the binary search algorithm operates correctly for different scenarios.

"""