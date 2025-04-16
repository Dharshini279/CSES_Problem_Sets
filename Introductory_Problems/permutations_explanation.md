### Description:
Given an integer `n`, construct a **beautiful permutation** of the integers `1, 2, ..., n` such that no two adjacent elements in the permutation differ by exactly 1. If it's impossible to construct such a permutation, output "NO SOLUTION".

### Approach:
This problem can be solved using a **greedy** approach:
- First, divide the numbers into **even** and **odd** numbers.
- If `n > 4`, the permutation can be formed by placing even numbers first (in descending order) followed by odd numbers (also in descending order). This avoids adjacent elements differing by 1.
- If `n == 4`, it's a special case where the permutation cannot be arranged without adjacent elements differing by 1, so we output a specific arrangement.
- If `n == 1`, the permutation is just `[1]`, which is trivially beautiful.
- If `n <= 3`, it's impossible to construct a beautiful permutation, so we output "NO SOLUTION".

### Time Complexity:
**O(n)** — The time complexity is linear because we are iterating over the numbers to split them into even and odd lists and then print them.

