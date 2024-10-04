class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill, remainder = divmod(sum(skill), len(skill) // 2)
        if remainder != 0:
            return -1
        chemistry = 0
        counter = dict()
        for s1 in skill:
            if s1 >= total_skill:
                return -1
            s2 = total_skill - s1
            if s2 not in counter:
                counter[s1] = counter.get(s1, 0) + 1
                continue
            chemistry += s1 * s2
            counter[s2] -= 1
            if counter[s2] == 0:
                del counter[s2]
        return chemistry if not counter else -1
