### Description:
The task is to find the maximum number of movies that can be watched entirely in a movie festival. You are given the start and end times of `n` movies, and you need to select the maximum number of non-overlapping movies to watch.

### Approach:
The approach used in this solution is **Greedy Algorithm**:
1. **Sort the Movies by Ending Time**: First, sort the movies by their end time. This is because to maximize the number of movies, it is optimal to always pick the movie that finishes the earliest.
2. **Iterate Over the Sorted Movies**: 
   - Keep track of the end time of the last movie watched.
   - For each movie, if its start time is greater than or equal to the end time of the last movie, you can watch it. In that case, increment the count of movies watched and update the end time to the current movie's end time.
3. **Return the Result**: After processing all movies, the count `c` will contain the maximum number of movies that can be watched without overlap.

### Time Complexity:
**O(n log n)** — The solution primarily involves sorting the movies by their end times, which takes **O(n log n)** time. The subsequent iteration over the movies takes **O(n)** time, so the overall time complexity is **O(n log n)**.

