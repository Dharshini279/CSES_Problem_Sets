### Description:
The task is to simulate the execution of an algorithm known as the **Collatz conjecture** for a given positive integer `n`. The algorithm follows these steps:
- If `n` is even, divide it by 2.
- If `n` is odd, multiply it by 3 and add 1.
- Repeat the steps until `n` becomes 1.

For example, the sequence for `n = 3` is:
`3 → 10 → 5 → 16 → 8 → 4 → 2 → 1`

### Approach:
This problem can be solved using a **while loop**:
1. Print the initial value of `n`.
2. Check if `n` is even or odd using the modulo operator (`n % 2`):
   - If `n` is even, divide it by 2.
   - If `n` is odd, multiply it by 3 and add 1.
3. Continue applying the algorithm until `n` becomes 1, printing `n` at each step.

### Time Complexity:
**O(log n)** — The time complexity is logarithmic because each step (for even `n`) reduces the value of `n` by half, leading to a logarithmic number of iterations until `n` reaches 1.

