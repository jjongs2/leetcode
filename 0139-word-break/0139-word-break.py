class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        memo = set()

        def is_possible(start):
            if start == length:
                return True
            for word in wordDict:
                if (end := start + len(word)) in memo:
                    continue
                if s.startswith(word, start) and is_possible(end):
                    return True
            memo.add(start)
            return False

        return is_possible(0)
