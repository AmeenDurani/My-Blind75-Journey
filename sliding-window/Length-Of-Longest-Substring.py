# Longest Substring Without Repeating Characters
# https://neetcode.io/problems/longest-substring-without-duplicates/question

# Complexity
# - Time: O(n)
# - Space: O(n)

# Code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = set()
        res = 0
        l = 0

        for r, ch in enumerate(s):
            while ch in h:
                h.remove(s[l])
                l += 1

            h.add(ch)
            res = max(res, r - l + 1)
        return res