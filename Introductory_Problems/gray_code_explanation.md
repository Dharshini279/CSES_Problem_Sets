### Description:
A **Gray code** is a sequence of 2ⁿ binary numbers of length `n` such that each consecutive number differs from the previous by **exactly one bit**. This minimizes transitions and is widely used in digital systems and error correction.

### Approach:
**Binary Reflected Gray Code (BRGC)**:
- Iterate from 0 to 2ⁿ - 1.
- For each integer `i`, compute the Gray code using:
  
  gray(i) = i XOR (i >> 1)

- Convert the result to a binary string and pad with leading zeros to make it `n` bits long.
- This guarantees that each pair of successive codes differs by only one bit.

### Time Complexity:
O(2ⁿ)

- We generate 2ⁿ codes, each computed in constant time.

