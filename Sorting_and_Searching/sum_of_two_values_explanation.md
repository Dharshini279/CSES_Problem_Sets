### Description:
The task is to find two distinct values in the array whose sum equals a given value `x`. The values must be at different positions, and if such a pair exists, we need to output the indices of these two values (1-based index). If no such pair exists, print "IMPOSSIBLE".

### Approach:
The approach used here is **Hashing**:
1. **Hash Map to Store Elements**: 
   - A dictionary `see` is used to keep track of the elements we have seen so far in the array and their corresponding indices.
2. **Iterate Over the Array**:
   - For each element `l[i]`, compute the complement `c = t - l[i]`, where `t` is the target sum.
   - Check if the complement `c` exists in the dictionary `see`. If it does, print the current index `i+1` (1-based index) and the stored index of `c` (which is `see[c] + 1`).
3. **Update Dictionary**:
   - If the complement is not found, store the current element `l[i]` and its index `i` in the dictionary.
4. **Handle Case with No Pair**:
   - If no valid pair is found after checking all elements, print "IMPOSSIBLE".

### Time Complexity:
**O(n)** — The solution performs a single pass through the array while checking for the complement using constant-time dictionary operations. Thus, the time complexity is **O(n)**, where `n` is the number of elements in the array.


