**Description of the Problem:**  
You are given `n` apples with known weights. The goal is to divide them into two groups such that the absolute difference between the total weights of the two groups is minimized.

**Approach Used:**  
- Brute-force using **subset generation** via `itertools.combinations`.
- Try all possible subsets.
- For each subset:
  - Let the sum be `s1`, then the second subset has sum `s2 = total - s1`.
  - The absolute difference is `abs(total - 2 * s1)`.
  - Keep track of the minimum difference.

🔎 This approach is similar to the **"Minimum Subset Sum Difference"** problem,  
which is a variation of the classic **Partition Problem** in dynamic programming —  
but here it is solved by brute-force using combinations.

**Time Complexity:**  

| Resource     | Complexity     |
|--------------|----------------|
| Time         | O(2ⁿ × n)       |
| Space        | O(1) extra (excluding input and combinations) |
