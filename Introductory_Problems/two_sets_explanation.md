### Description:
The task is to determine whether the numbers `1, 2, ..., n` can be divided into two sets with **equal sums**. If such a division is possible, print the two sets; otherwise, output "NO".

### Approach:
This problem can be solved using the **Greedy** approach:
1. Calculate the **total sum** of the numbers from `1` to `n` using the formula `n * (n + 1) / 2`.
2. If the sum is **odd**, it's impossible to divide it into two equal sets, so output "NO".
3. If the sum is **even**, the task becomes finding two subsets that each have half of the total sum. We can achieve this by starting from the largest number (`n`) and trying to add it to one subset (`a1`) while ensuring the sum of that subset does not exceed half of the total sum.
4. The numbers not included in `a1` go into the second subset (`a2`).

### Time Complexity:
**O(n)** — The algorithm processes the numbers from `n` to `1`, and thus the time complexity is linear in terms of `n`.

