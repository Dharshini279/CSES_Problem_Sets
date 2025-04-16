### Description:
The task is to determine the number of rounds required to collect the numbers in increasing order from a given array that contains each number from 1 to `n` exactly once. You are also given `m` operations that swap two numbers in the array, and after each swap operation, you need to report the number of rounds.

### Approach:
This problem can be tackled by simulating the process of collecting numbers in increasing order using the **Greedy** approach with an array and **Dynamic Programming** to track the position of numbers:

1. **Initial Setup**: First, the algorithm calculates the initial number of rounds by checking the positions of numbers from 1 to `n`. The idea is to iterate over the array and check if any number is out of order (i.e., not in increasing order).
   
2. **Simulating the Swaps**:
   - After each swap, the algorithm needs to determine the new number of rounds. To do this:
     - Track the positions of the swapped numbers using a `dp` array.
     - Update the positions of the swapped numbers in the `dp` array.
     - Recalculate the number of rounds after each swap by checking if the positions of the swapped numbers are still in increasing order.
   
3. **Optimizing the Calculation**:
   - For each swap, only the affected numbers need to be checked. This minimizes the number of checks needed after each operation.
   
4. **Output**:
   - After each swap, the algorithm prints the current number of rounds.

### Time Complexity:
The time complexity of the solution is **O(n + m)**:
- The initial setup takes **O(n)** time to fill the `dp` array and calculate the initial rounds.
- Each swap operation involves updating positions and checking adjacent positions, which is efficient due to only needing to check a small number of elements each time.
  
Thus, the total time complexity is **O(n + m)**, where `n` is the size of the array and `m` is the number of operations.


