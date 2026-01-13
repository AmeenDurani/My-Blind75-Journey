# 3Sum
# https://neetcode.io/problems/three-integer-sum/question

# Complexity
# - Time: O(n^2)
# - Space: O(n) or O(1)

# Code
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        l = len(nums)

        for i in range(l):
            
            # Skip if we've already seen this starting number before
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, l - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                # Found the target triplet
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Increment if we saw this before
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Decrement if we saw this before
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < 0:
                    # Increment left 
                    left += 1
                elif s > 0:
                    # Decrement right
                    right -= 1
        
        return res