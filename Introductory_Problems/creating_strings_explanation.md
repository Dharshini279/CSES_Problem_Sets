**Description of the Problem:**  
Given a string, your task is to generate all different strings that can be created using its characters. This means finding all unique permutations of the string.

**Approach Used:**  
**Brute Force** approach is used to generate all possible permutations of the given string.  
  - The `permutations(n, len(n))` function from Python's `itertools` library is used to generate all permutations of the string.  
  - The permutations are stored in a list and converted into a set to remove duplicate permutations.  
  - The unique permutations are then sorted alphabetically and printed.

**Time Complexity:**  
- **Time:** O(n! * n) — There are `n!` permutations for a string of length `n`, and generating each permutation takes O(n) time.  
- **Space:** O(n!) — Storing all permutations requires space proportional to the number of unique permutations.

