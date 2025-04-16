### Description:
Given a string, the task is to reorder its letters in such a way that it forms a **palindrome**. A palindrome reads the same forwards and backwards. A palindrome can have at most one letter with an odd frequency.

### Approach:
This solution uses the **Greedy** approach:

1. **Character Frequency Count**:  
   - Count the frequency of each character in the string using a dictionary.

2. **Check Odd Frequencies**:  
   - If more than one character has an odd frequency, it's **impossible** to form a palindrome. In this case, print "NO SOLUTION".
   - If only one or zero characters have an odd frequency, a palindrome can be formed.

3. **Construct Palindrome**:  
   - For characters with **even frequency**, place half of them in the first half of the string.
   - If there's a character with an **odd frequency**, place it in the center of the palindrome.
   - The second half of the palindrome is the reverse of the first half.

4. **Return Result**:  
   - Combine the first half, middle character (if any), and the reversed first half to form the final palindrome.

### Time Complexity:
**O(n)** — The string is processed once to build the frequency map, and then sorting and constructing the palindrome takes linear time.

