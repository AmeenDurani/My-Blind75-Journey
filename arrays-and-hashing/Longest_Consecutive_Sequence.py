# Longest Consecutive Sequence
# https://neetcode.io/problems/longest-consecutive-sequence/question

# Complexity
# - Time: O(n)
# - Space: O(n)

# Code
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        
        for num in s:
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                longest = max(length, longest)
        return longest