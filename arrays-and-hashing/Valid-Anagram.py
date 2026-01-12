# Valid Anagram
# https://neetcode.io/problems/is-anagram/question

# Complexity
# - Time: O(n + m)
# - Space: O(1)

# Code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        d1, d2 = {}, {}

        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        
        return d1 == d2