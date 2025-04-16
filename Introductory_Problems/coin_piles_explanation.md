**Description of the Problem:**  
You are given two coin piles containing `a` and `b` coins. In each move, you can:
- Remove one coin from the left pile and two coins from the right pile, or
- Remove two coins from the left pile and one coin from the right pile.

The task is to determine if it’s possible to empty both piles by performing these moves.

**Approach Used:**  
This problem is best approached using a **Greedy** strategy, combined with **mathematical reasoning**.

- The core idea is that in each move, you are reducing 3 coins in total (either as 1 from the left and 2 from the right, or 2 from the left and 1 from the right). Thus, the total number of coins must be divisible by 3.
  
- For the solution to be possible:
  - The sum of the coins in both piles (`a + b`) must be divisible by 3. If not, it's impossible to perform the required operations.
  - The smaller pile must be large enough to perform the necessary moves without exhausting coins from one pile prematurely. The condition `min(a, b) * 2 >= max(a, b)` ensures that both piles can contribute to the moves equally.

**Time Complexity:**  
- **Time:** O(t), where `t` is the number of test cases. Each test case requires constant time to check the two conditions (`(a + b) % 3 == 0` and `min(a, b) * 2 >= max(a, b)`).
- **Space:** O(1)

