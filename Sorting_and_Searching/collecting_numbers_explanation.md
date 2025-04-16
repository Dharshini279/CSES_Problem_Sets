### Description:
The task is to collect the numbers from 1 to `n` in increasing order from an array that contains each number from 1 to `n` exactly once. On each round, traverse the array from left to right and collect as many numbers as possible in the increasing order.

The goal is to determine how many rounds it will take to collect the numbers in the desired order.

### Approach:
This problem can be solved using a **Greedy** approach with a **DP** (Dynamic Programming)-like strategy:
1. First, create a `dp` array to store the index positions of each number in the array.
2. Traverse the array and fill the `dp` array where `dp[i]` represents the index of the number `i` in the array.
3. Initialize the number of rounds (`ans`) to 1.
4. Then, iterate through numbers `2` to `n` and check if the position of the current number (`dp[i]`) is before the previous number (`dp[i-1]`). If it is, it means a new round is needed, so increment the `ans`.
5. The result will be the total number of rounds.

### Time Complexity:
**O(n)** — The algorithm processes each element of the array a constant number of times, making the time complexity linear with respect to `n`.

