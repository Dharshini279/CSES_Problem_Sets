### Description:
The task is to find the longest sequence of successive songs from a playlist where each song is unique. Given `n` songs in the playlist, the goal is to identify the maximum length of a subsequence where no song repeats.

### Approach:
The approach used in this solution is **Sliding Window Technique**:
1. **Use Two Pointers (Sliding Window)**: 
   - The variable `l` represents the left pointer of the window, and `r` represents the right pointer. The window `[l, r]` represents a subarray of unique songs.
2. **Set to Track Unique Songs**: 
   - Use a set `vis` to store the unique songs within the current window.
3. **Expand the Right Pointer**: 
   - For each song at position `r`, if the song is not in the set, add it to the set.
   - If the song is already in the set, increment the left pointer `l` and remove songs from the set until the current song can be added without repetition.
4. **Update Maximum Length**: 
   - At each step, update the maximum length of the window (`m`), which is the size of the current valid subarray.
5. **Return Result**: After iterating through the playlist, `m` will store the longest subsequence length of unique songs.

### Time Complexity:
**O(n)** — The solution processes each song at most twice (once when adding to the set and once when removing from it), so the overall time complexity is **O(n)**, where `n` is the number of songs.


