### Description:
The task is to calculate the number of **trailing zeros** in the factorial of a given number `n`. A trailing zero in a number is created by multiplying 10, which is the product of 2 and 5. Since there are always more factors of 2 than factors of 5 in the factorial of a number, the problem reduces to counting how many times 5 is a factor in the numbers from 1 to `n`.

### Approach:
This problem can be solved using a **Greedy** approach:
- To find the number of trailing zeros, count how many multiples of 5, 25, 125, etc., exist up to `n`. This is because each multiple of 5 contributes at least one factor of 5.
- Start with `i = 5` and keep increasing `i` by multiplying it by 5, counting how many times `n // i` can fit into `n` (this represents how many numbers are divisible by 5, 25, 125, etc.).
- Continue this until `i` exceeds `n`.

### Time Complexity:
**O(log n)** — The number of times we divide by powers of 5 is logarithmic with respect to `n`, specifically **O(log₅(n))**.

