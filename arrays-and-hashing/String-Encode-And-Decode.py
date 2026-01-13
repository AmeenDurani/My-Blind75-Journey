# String Encode And Decode
# https://neetcode.io/problems/string-encode-and-decode/question

# Complexity
# - Time: O(m)
# - Space: O(m + n)

# Code
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            # format -> <len>_<string>
            res += str(len(string)) + '_'
            res += string
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[i] != '_':
                i += 1
            
            count = int(s[j:i])
            res.append(s[i+1 : i+1+count])
            i += 1 + count
        return res



            


# Rough work

# ["Hello", "World"]
# We can encode using a number followed by any character. IN this solution, use '_'.
# encoded = 5_Hello5_World
# We can decode by reading the number, terminated by the character '_'. Then appending said character.
# decoded = ["Hello", "World"]