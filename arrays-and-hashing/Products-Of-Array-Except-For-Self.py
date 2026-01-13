# Products of Array Except Self
# https://neetcode.io/problems/products-of-array-discluding-self/question

# Complexity
# - Time: O(n)
# - Space: O(n)

# Code
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prod = 1
        
        # traverse left->right
        for i in range(n):
            res[i] = prod
            prod *= nums[i]

        # reset prod
        prod = 1

        # traverse right-> left
        for i in range(n - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        
        return res