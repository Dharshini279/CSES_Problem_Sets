### Description:
Given coordinates `(y, x)` in a **number spiral**, an infinite grid where numbers start from 1 at the top-left and grow in a square spiral pattern outward, the task is to find the number at the given position `(y, x)`.

### Approach:
The number spiral follows a pattern:
- Each layer of the spiral forms a square with side length `n = max(x, y)`.
- The **last number** in layer `n` is `n*n`.
- If `n` is **even**:
  - If `y == n` (bottom row of the layer), the number is `n*n - x + 1`.
  - Otherwise, the number is `(n-1)^2 + y`.
- If `n` is **odd**:
  - If `x == n` (rightmost column), the number is `n*n - y + 1`.
  - Otherwise, the number is `(n-1)^2 + x`.

This approach calculates the number directly using mathematical formulas.

### Time Complexity:
**O(1)** per test case — the result is computed using constant-time mathematical operations.
Total complexity: **O(t)** for `t` test cases.

