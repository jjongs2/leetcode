class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [set() for _ in range(n)]
        for v1, v2 in edges:
            answer[v2].add(v1)
        for i, ancestors in enumerate(answer):
            stack = list(ancestors)
            while stack:
                v = stack.pop()
                if v > i:
                    for u in answer[v]:
                        if u not in ancestors:
                            stack.append(u)
                ancestors |= answer[v]
        return [sorted(ancestors) for ancestors in answer]
