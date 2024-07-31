from math import inf


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        book_count = len(books)
        dp = [inf for _ in range(book_count + 1)]
        dp[0] = 0
        for i in range(1, book_count + 1):
            width, height = 0, 0
            for j in range(i - 1, -1, -1):
                w, h = books[j]
                width += w
                if width > shelfWidth:
                    break
                height = max(height, h)
                dp[i] = min(dp[i], dp[j] + height)
        return dp[-1]
