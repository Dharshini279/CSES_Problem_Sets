### Description:
You are given a **DNA sequence** consisting of characters `A`, `C`, `G`, and `T`. The task is to find the **longest repetition** in the sequence, i.e., the maximum length of a substring where all characters are the same.

### Approach:
This problem uses a **Greedy** approach:
- Iterate through the string and compare each character with the previous one.
- Keep track of the current length of consecutive characters (repetition).
- If the current character matches the previous one, increment the repetition length.
- If the characters don't match, reset the repetition count to 1.
- Continuously update the maximum repetition length as you go through the string.

### Time Complexity:
**O(n)** — We only need one pass through the string, making the time complexity linear with respect to the length of the DNA sequence.

