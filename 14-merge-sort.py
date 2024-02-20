def merge_sort(arr):
    """
    Perform merge sort to sort the elements of the array in ascending order.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr)

"""
Theory Question:
Explain the concept of merge sort and its role in computer science algorithms. 
Describe how merge sort works, including its divide-and-conquer approach, splitting, merging, and recursion. 
Discuss the advantages and disadvantages of merge sort compared to other sorting algorithms, such as quick sort and insertion sort.

Practical Question:
Design a Python program that demonstrates the use of merge sort to sort a list of elements. The program should have the following functionalities:

Allow the user to input a list of elements to be sorted.
Implement the merge sort algorithm to sort the elements in ascending order.
Display the sorted list of elements after the merge sort operation is completed.
Include validation checks to ensure that the user inputs are in the correct format and that the merge sort algorithm operates correctly for different scenarios.
"""