### Description:
The task is to count the number of ways to place two knights on a `k x k` chessboard for each `k = 1, 2, ..., n` such that the two knights do not attack each other.

### Approach:
This problem can be solved using the **Mathematical and Combinatorial** approach:
1. The total number of ways to place two knights on a `k x k` chessboard without any restriction is given by the formula `n = (k^2 * (k^2 - 1)) // 2`. This counts all pairs of cells.
2. The number of ways in which the knights **attack** each other is determined by how many possible attacking positions exist. A knight can attack in 8 possible ways. On a `k x k` board, the number of attacking pairs is `4 * (k - 1) * (k - 2)` for `k > 2`.
3. Subtract the attacking pairs from the total pairs to get the number of valid configurations where the knights do not attack each other.

### Time Complexity:
**O(t)** — The algorithm runs for each test case `k = 1` to `t`, and for each `k`, the computation takes constant time, so the time complexity is linear in terms of `t`.
