# Two Sum
# https://neetcode.io/problems/two-integer-sum/question

# Complexity
# - Time: O(n)
# - Space: O(n)

# Code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in d:
                return [d.get(need), i]
            else:
                d[num] = i
        return []

