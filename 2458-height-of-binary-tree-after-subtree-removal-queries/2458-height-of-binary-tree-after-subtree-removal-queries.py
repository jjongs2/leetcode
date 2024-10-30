from collections import defaultdict
from heapq import heappush, heapreplace


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.depth = 0
        self.height = 0


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max_heights = defaultdict(list)
        precomputed = dict()

        def find_height(node, depth):
            if node is None:
                return 0
            height = max(
                find_height(node.left, depth + 1), find_height(node.right, depth + 1)
            )
            heap = max_heights[depth]
            if len(heap) < 2:
                heappush(heap, height)
            elif height > heap[0]:
                heapreplace(heap, height)
            node.depth = depth
            node.height = height
            return height + 1

        def precompute(node):
            if node is None:
                return
            max_height = -1
            heap = max_heights[node.depth]
            if len(heap) == 2:
                max_height = heap[1] if node.height < heap[1] else heap[0]
            precomputed[node.val] = node.depth + max_height
            precompute(node.left)
            precompute(node.right)

        find_height(root, 0)
        precompute(root)
        return [precomputed[query] for query in queries]
