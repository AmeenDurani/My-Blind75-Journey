# Container With Most Water
# https://neetcode.io/problems/max-water-container/question

# Complexity
# - Time: O(n)
# - Space: O(1)

# Code
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        array_length = len(heights)             # Cache this for optimal look-up time.
        L, R = 0, array_length - 1              # Start on opposing sides of the List.
        res = min(heights[L], heights[R]) * R   # Return variable, initialized to starting area.
        
        # Iterate as long as the width is not zero.
        while L < R:
            if heights[R] < heights[L]:
                R -= 1
            elif heights[L] <= heights[R]:
                L += 1
            current_area = min(heights[R], heights[L]) * (R - L)
            res = max(res, current_area)
        
        return res




# Thoughts here:

# Area calculation: width (j - i) multiplied by the minimum of the heights h[j] and h[i]

# Brute force is O(n^2), where for each bar, we'd iterate left to right, tracking the max for each index i. This is O(1) of space

# Optimized solution, we start with pointers on each side, L and R. Sicne area is limited by the shortest wall,
# we move the pointer who's wall is the shortest inwards. 

# Personal notes: Greedy doesn't work here. For example, if we decide which wall to move based on finding a taller wall, we'd still be limited by the shorter wall,
# and will actually decrease the area. And if we try to maximize area by looking ahead, this is effectively O(n^2).
