### Description:
The task is to calculate the number of distinct values in a list of `n` integers. 

### Approach:
The approach used in this solution is **Sorting + Linear Traversal**:
1. **Sort the Array**: First, the array is sorted so that all duplicate elements are adjacent to each other.
2. **Linear Traversal**: After sorting, we traverse the array and count distinct elements by checking if the current element is different from the previous one.
3. **Final Count**: The number of distinct values is printed after the traversal.

### Time Complexity:
**O(n log n)** — Sorting the array takes **O(n log n)** time, and the subsequent linear traversal to count distinct elements takes **O(n)** time. Thus, the overall time complexity is **O(n log n)**.


