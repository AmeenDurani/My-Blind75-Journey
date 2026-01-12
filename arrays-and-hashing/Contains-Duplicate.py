# Contains Duplicate
# https://neetcode.io/problems/duplicate-integer/question

# Complexity
# - Time: O(n)
# - Space: O(n)

# Code
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for var in nums:
            if var in hashset:
                return True
            else:
                hashset.add(var)
        return False