### Description:
The task is to find the maximum sum of values in a contiguous, nonempty subarray of the given array. This problem is a typical example of the **Kadane's Algorithm**.

### Approach:
The approach used in this solution is **Kadane's Algorithm**:
1. **Initialize Variables**: 
   - `c` is used to store the maximum sum of the current subarray at each index.
   - `m` is used to store the global maximum sum.
2. **Iterate through the Array**: For each element in the array:
   - Update `c` by choosing the larger value between the current element and the sum of the current subarray plus the element.
   - Update `m` to store the maximum of `m` and `c`.
3. **Return Result**: After completing the traversal, `m` holds the maximum sum of any contiguous subarray.

### Time Complexity:
**O(n)** — The solution iterates through the array exactly once, making it an **O(n)** time complexity algorithm, where `n` is the number of elements in the array.


