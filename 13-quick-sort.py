def partition(arr, low, high):
    """
    Partition the array and return the index of the pivot element.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """
    Perform quick sort to sort the elements of the array in ascending order.
    """
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

"""
Theory Question:
Explain the concept of quick sort and its role in computer science algorithms. 
Describe how quick sort works, including its divide-and-conquer approach, pivot selection, and partitioning steps. 
Discuss the advantages and disadvantages of quick sort compared to other sorting algorithms, such as merge sort and insertion sort.

Practical Question:
Design a Python program that demonstrates the use of quick sort to sort a list of elements. The program should have the following functionalities:

Allow the user to input a list of elements to be sorted.
Implement the quick sort algorithm to sort the elements in ascending order.
Display the sorted list of elements after the quick sort operation is completed.
Include validation checks to ensure that the user inputs are in the correct format and that the quick sort algorithm operates correctly for different scenarios.
"""