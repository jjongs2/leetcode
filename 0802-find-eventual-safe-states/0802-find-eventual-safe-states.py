class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        states = [-1] * n

        def is_safe(node):
            if states[node] != -1:
                return states[node] == 1
            states[node] = 0
            for next_node in graph[node]:
                if not is_safe(next_node):
                    return False
            states[node] = 1
            return True

        return [i for i in range(n) if is_safe(i)]
