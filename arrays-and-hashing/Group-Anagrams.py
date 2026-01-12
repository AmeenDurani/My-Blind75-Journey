# Group Anagrams
# https://neetcode.io/problems/anagram-groups/question

# Complexity
# - Time: O(m * n)
# - Space: O(m + m * n)

# Code
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            tracker = [0] * 26 # 26 letters, track the frequency of each
            for char in string:
                tracker[ord(char) - ord('a')] += 1
            res[tuple(tracker)].append(string)
        
        return list(res.values())