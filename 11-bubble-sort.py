def bubble_sort(arr):
    """
    Perform bubble sort to sort the elements of the array in ascending order.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)

"""
Theory Question:
Explain the concept of bubble sort and its role in computer science algorithms. 
Describe how bubble sort works, including its algorithmic complexity and comparison-based nature. 
sDiscuss the advantages and disadvantages of bubble sort compared to other sorting algorithms, such as quicksort and mergesort.

Practical Question:
Design a Python program that demonstrates the use of bubble sort to sort a list of elements. The program should have the following functionalities:

Allow the user to input a list of elements to be sorted.
Implement the bubble sort algorithm to sort the elements in ascending order.
Display the sorted list of elements after the bubble sort operation is completed.
Include validation checks to ensure that the user inputs are in the correct format and that the bubble sort algorithm operates correctly for different scenarios.

"""