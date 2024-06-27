class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(c for c in s.lower() if c.isalnum())
        return filtered == filtered[::-1]
