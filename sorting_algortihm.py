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

# Test the Merge Sort algorithm
if __name__ == "__main__":
    # Example data to test
    data = [28, 17, 33, 6, 8, 52, 20]
    print("Unsorted Array:", data)
    sorted_data = merge_sort(data)
    print("Sorted Array:", sorted_data)
