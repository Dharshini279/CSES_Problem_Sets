### Description:
You're given an array of `n` integers, and the task is to make the array **non-decreasing** — meaning each element should be at least as large as the one before it.
You can only **increase** elements (by 1 per move), and you need to find the **minimum number of moves** to achieve this.

### Approach:
We use a **greedy approach**:
- Traverse the array from left to right.
- If the current element is **less than** the previous one, calculate the difference.
- Add that difference to the total moves.
- Update the current element to match the previous one (so the array remains non-decreasing).

This way, we ensure the array is fixed with the minimum number of increases.

### Time Complexity:
**O(n)** — since we go through the array just once, with constant time operations at each step.

