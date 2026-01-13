# Valid Palindrome
# https://neetcode.io/problems/is-palindrome/question

# Complexity
# - Time: O(n)
# - Space: O(1)

# Code
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, l = 0, len(s)
        j = l - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True