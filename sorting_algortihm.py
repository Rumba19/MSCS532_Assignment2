# Merge Sort Implementation
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
    sorted_data = merge_sort(data)
    merge_sorted_array = f"Sorted array using Merge sort = {sorted_data}"
    sorted_data = quick_sort(data)
    quick_sorted_array = f"Sorted array using quick Sort = {sorted_data}"
    print(merge_sorted_array, quick_sorted_array)
