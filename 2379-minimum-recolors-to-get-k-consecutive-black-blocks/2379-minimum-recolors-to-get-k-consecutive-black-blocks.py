class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_count = count = blocks[:k].count("W")
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                count += 1
            if blocks[i - k] == "W":
                count -= 1
            min_count = min(min_count, count)
        return min_count
