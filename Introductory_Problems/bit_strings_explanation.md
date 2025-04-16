**Description of the Problem:**  
You are given an integer `n`. The task is to calculate how many binary strings (bit strings) of length `n` exist.  
A bit string consists only of 0s and 1s. For example, for n = 3, the total number of such strings is 2³ = 8.

**Approach Used:**  
- For each of the `n` positions, there are 2 choices (either 0 or 1).
- Hence, the total number of bit strings of length `n` is `2ⁿ`.
- To avoid large numbers, take the result modulo **10⁹ + 7**, a common modulus in programming contests.

**Time Complexity:**  
- **Time:** O(log n) if using built-in `pow(2, n, m)`  
- **(This code uses `2**n`, so in Python it works efficiently but may be O(n) in other languages)**  
- **Space:** O(1)

