class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        indices = dict()
        for right, char in enumerate(s):
            if (index := indices.get(char, -1)) >= left:
                left = index + 1
            indices[char] = right
            max_length = max(max_length, right - left + 1)
        return max_length
