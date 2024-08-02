from collections import Counter
from itertools import chain, product

DIRECTIONS = ((-1, 0), (0, -1), (0, 1), (1, 0))


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_length = len(word)
        m, n = len(board), len(board[0])
        if m * n < word_length:
            return False
        board_counter = Counter(chain.from_iterable(board))
        if any(board_counter[char] < count for char, count in Counter(word).items()):
            return False
        if board_counter[word[-1]] < board_counter[word[0]]:
            word = word[::-1]

        def search(r, c, depth):
            if depth == word_length:
                return True
            if not (0 <= r < m and 0 <= c < n):
                return False
            if board[r][c] != word[depth]:
                return False
            temp, board[r][c] = board[r][c], ""
            result = any(search(r + dr, c + dc, depth + 1) for dr, dc in DIRECTIONS)
            board[r][c] = temp
            return result

        return any(search(r, c, 0) for r, c in product(range(m), range(n)))
