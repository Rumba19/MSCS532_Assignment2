
# Sorting Algorithm Comparison: Quick Sort vs Merge Sort

This project implements and compares two popular divide-and-conquer sorting algorithms: **Quick Sort** and **Merge Sort**. The comparison evaluates their performance on datasets of different types and sizes, providing insights into their practical applications.

---

## **Definitions**

### **Quick Sort**
Quick Sort is a highly efficient sorting algorithm that works by partitioning the input array around a pivot element. The array is divided into two subarrays:
- Elements smaller than the pivot.
- Elements greater than the pivot.

These subarrays are recursively sorted. The algorithm is in-place and does not require additional memory for intermediate results.

**Time Complexity**:
- Best Case: \(O(n \log n)\)
- Average Case: \(Θ(n \log n)\)
- Worst Case: \(O(n^2)\) (occurs when partitions are unbalanced)

### **Merge Sort**
Merge Sort is a stable sorting algorithm that recursively divides the array into two halves, sorts each half, and then merges the sorted halves into a single sorted array. It requires additional memory for the merging process.

**Time Complexity**:
- Best Case: \(Θ(n \log n)\)
- Average Case: \(Θ(n \log n)\)
- Worst Case: \(Θ(n \log n)\)

---

## **Comparison**

### **Performance Metrics**
The algorithms were tested on datasets of varying sizes and structures:
1. **Sorted Data**: Already sorted in ascending order.
2. **Reverse-Sorted Data**: Sorted in descending order.
3. **Random Data**: Randomly shuffled numbers.

### **Key Observations**
| Algorithm   | Dataset Type       | Time Complexity | Memory Usage  | Stability |
|-------------|--------------------|-----------------|---------------|-----------|
| Quick Sort  | Random Data        | \(Θ(n \log n)\) | Low (in-place)| Not Stable|
| Quick Sort  | Sorted/Reverse Data| \(O(n^2)\)      | Low (in-place)| Not Stable|
| Merge Sort  | All Data Types     | \(Θ(n \log n)\) | High          | Stable    |

- **Quick Sort**: Performs better on average for random data but can degrade significantly for sorted or reverse-sorted inputs.
- **Merge Sort**: Consistent performance across all input types but requires additional memory for merging.

---
This project was inspired by standard implementations of Quick Sort and Merge Sort from GeeksforGeeks and Python's official documentation.

