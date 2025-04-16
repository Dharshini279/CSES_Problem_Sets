### Description:
You're given a list of numbers from `1` to `n` with exactly **one number missing**.  
Your task is to **find and print the missing number** from the list.

### Approach:
We use the **mathematical formula for the sum** of the first `n` natural numbers:

    Total sum = n * (n + 1) // 2

- Calculate the actual sum of the given numbers.
- Subtract this from the total expected sum.
- The difference is the **missing number**.

This is an efficient and simple approach that avoids extra space or complex logic.

### Time Complexity:
**O(n)** — because we compute the sum of the input list, which requires a single pass through the list.

