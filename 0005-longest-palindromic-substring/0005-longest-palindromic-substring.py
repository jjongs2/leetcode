class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        def find_palindrome(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            return left, right - left

        start, size = 0, 1
        for i in range(length):
            start1, size1 = find_palindrome(i - 1, i + 1)
            start2, size2 = find_palindrome(i - 1, i)
            if size1 > size:
                start, size = start1, size1
            if size2 > size:
                start, size = start2, size2
        return s[start : start + size]
