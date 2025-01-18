# Merge Sort Implementation
import random
import time


def merge_sort(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the two sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves and build the sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left or right half
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort Implementation
def quick_sort(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Select the pivot (middle element)
    pivot = arr[len(arr) // 2]

    # Partition into three parts: less, equal, greater
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right partitions
    return quick_sort(left) + middle + quick_sort(right)

# Function invocation
if __name__ == "__main__":
    #Hard Coded data
    data = [28, 17, 33, 6, 8, 52, 20]
    unsorted = f"Unsorted array = {data}"
    print(unsorted)
     # Merge Sort
    start = time.time()
    merge_sorted_data = merge_sort(data)
    end = time.time()
    merge_sorted_array = f" Merge sorted = {merge_sorted_data}, Time: {end - start:.6f}s"
    print(merge_sorted_array)
     
     # Quick Sort
    start = time.time()
    quick_sorted_data = quick_sort(data)
    end = time.time()
    quick_sorted_array = f"Sorted array using quick Sort = {quick_sorted_data},Time: {end - start:.6f}s"
    print(quick_sorted_array)
