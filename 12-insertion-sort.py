def insertion_sort(arr):
    """
    Perform insertion sort to sort the elements of the array in ascending order.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)

"""
Theory Question:
Explain the concept of insertion sort and its role in computer science algorithms. 
Describe how insertion sort works, including its algorithmic complexity and comparison-based nature. 
Discuss the advantages and disadvantages of insertion sort compared to other sorting algorithms, such as bubble sort and selection sort.

Practical Question:
Design a Python program that demonstrates the use of insertion sort to sort a list of elements. The program should have the following functionalities:

Allow the user to input a list of elements to be sorted.
Implement the insertion sort algorithm to sort the elements in ascending order.
Display the sorted list of elements after the insertion sort operation is completed.
Include validation checks to ensure that the user inputs are in the correct format and that the insertion sort algorithm operates correctly for different scenarios.

"""