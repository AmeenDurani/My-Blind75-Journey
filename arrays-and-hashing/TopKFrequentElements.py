# Top K Frequent Elements
# https://neetcode.io/problems/top-k-elements-in-list/question

# Complexity
# - Time: O(n)
# - Space: O(n)

# Code
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = [[] for i in range(len(nums) + 1)] # len + 1 since we can have exactly the lenght of nums of frequency

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, value in count.items():
            res[value].append(key)
        
        out = []
        for i in range(len(res) - 1, 0, -1): # -second param 0 since we don't check 0 frequency numbers
            for num in res[i]:
                out.append(num)
                if len(out) == k:
                    return out
