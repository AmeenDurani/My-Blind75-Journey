# Best Time to Buy and Sell Stock
# https://neetcode.io/problems/buy-and-sell-crypto/question

# Complexity
# - Time: O(n)
# - Space: O(1)

# Code
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 10 ** 6
        res = 0
        
        for r in prices:
            if r < l:
                l = r
            elif r - l > res:
                res = r - l
        return res